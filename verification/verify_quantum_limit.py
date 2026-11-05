#!/usr/bin/env python3
"""Finite numerical checks for science/quantum_limit.md.

The checks compare interval field overlaps reconstructed from a channel's Choi
matrix with Bloch formulas, evaluate the finite-partition discrimination bound,
and compare Poisson-age quadrature with the exact renewal expression.

They do not prove the continuum-output theorem or certify arbitrary receivers.
The analytical argument, including the physical genie, is in the science page.

Usage from the repository root:
    python verification/verify_quantum_limit.py
    python verification/verify_quantum_limit.py --output quantum_limit_checks.json

Dependencies: NumPy and SciPy. The script does not depend on its working directory.
"""

from __future__ import annotations

import argparse
import json
from pathlib import Path

import numpy as np
import scipy
from scipy.integrate import quad
from scipy.linalg import expm


IDENTITY = np.eye(2, dtype=complex)
PAULI_X = np.array([[0, 1], [1, 0]], dtype=complex)
PAULI_Z = np.diag([1.0, -1.0]).astype(complex)
ABSOLUTE_TOLERANCE = 1.0e-10


def interval_data(omega: float, gamma: float, duration: float) -> dict:
    """Build a reduced channel, then reconstruct its interval field overlaps.

    A minimal Stinespring environment obtained from the Choi matrix has the same
    overlaps as the actual vacuum output. No field time discretization is used.
    """
    hamiltonian = omega * PAULI_X / 2

    def generator(matrix: np.ndarray) -> np.ndarray:
        return (
            -1j * (hamiltonian @ matrix - matrix @ hamiltonian)
            + gamma * (PAULI_Z @ matrix @ PAULI_Z - matrix)
        )

    columns = []
    for index in range(4):
        basis = np.zeros(4, dtype=complex)
        basis[index] = 1
        columns.append(
            generator(basis.reshape((2, 2), order="F")).reshape(4, order="F")
        )
    channel = expm(np.stack(columns, axis=1) * duration)

    def evolve(matrix: np.ndarray) -> np.ndarray:
        return (channel @ matrix.reshape(4, order="F")).reshape(
            (2, 2), order="F"
        )

    choi = np.zeros((4, 4), dtype=complex)
    for initial_row in range(2):
        for initial_column in range(2):
            matrix = np.zeros((2, 2), dtype=complex)
            matrix[initial_row, initial_column] = 1
            choi[
                2 * initial_row : 2 * initial_row + 2,
                2 * initial_column : 2 * initial_column + 2,
            ] = evolve(matrix)

    eigenvalues, eigenvectors = np.linalg.eigh((choi + choi.conj().T) / 2)
    # Only roundoff-level negative eigenvalues may be removed. Their minimum is
    # reported and checked by the caller, so this does not hide a CP failure.
    kraus = [
        np.sqrt(value) * eigenvectors[:, index].reshape((2, 2), order="F")
        for index, value in enumerate(eigenvalues)
        if value > 0
    ]

    def field(final_sign: int, initial_sign: int) -> np.ndarray:
        return np.array([operator[final_sign, initial_sign] for operator in kraus])

    stay_plus = field(0, 0)
    flip_plus = field(1, 0)
    stay_minus = field(1, 1)
    probability = float(np.vdot(flip_plus, flip_plus).real)
    overlap_c = np.vdot(stay_plus, flip_plus)
    overlap_a = np.vdot(stay_plus, stay_minus)

    bloch_generator = np.array([[-2 * gamma, -omega], [omega, 0.0]])
    bloch_channel = expm(bloch_generator * duration)
    trace_preserving_residual = np.max(
        np.abs(sum(operator.conj().T @ operator for operator in kraus) - IDENTITY)
    )
    return {
        "p": probability,
        "c": overlap_c,
        "a": overlap_a,
        "p_formula": (1 - bloch_channel[1, 1]) / 2,
        "c_formula": 1j * bloch_channel[0, 1] / 2,
        "a_formula": (
            np.exp(-2 * gamma * duration) + bloch_channel[0, 0]
        ) / 2,
        "minimum_choi_eigenvalue": float(eigenvalues[0]),
        "trace_preserving_residual": float(trace_preserving_residual),
    }


def check_intervals(rng: np.random.Generator, samples: int) -> dict:
    maximum_errors = {"p": 0.0, "c": 0.0, "a": 0.0}
    maximum_positive_bound_residuals = {
        "population": 0.0,
        "c_squared": 0.0,
        "a_squared": 0.0,
    }
    minimum_choi_eigenvalue = 0.0
    maximum_trace_preserving_residual = 0.0
    violations = []

    for _ in range(samples):
        omega = 10 ** rng.uniform(-2, 1)
        gamma = 10 ** rng.uniform(-2, 1)
        duration = 10 ** rng.uniform(-3, 1)
        data = interval_data(omega, gamma, duration)
        parameters = {"omega": omega, "gamma": gamma, "duration": duration}

        for name in maximum_errors:
            error = float(abs(data[name] - data[f"{name}_formula"]))
            maximum_errors[name] = max(maximum_errors[name], error)
            if error > ABSOLUTE_TOLERANCE:
                violations.append(
                    {"check": f"{name}_identity", "residual": error, **parameters}
                )

        minimum_choi_eigenvalue = min(
            minimum_choi_eigenvalue, data["minimum_choi_eigenvalue"]
        )
        maximum_trace_preserving_residual = max(
            maximum_trace_preserving_residual, data["trace_preserving_residual"]
        )
        if data["minimum_choi_eigenvalue"] < -ABSOLUTE_TOLERANCE:
            violations.append({"check": "choi_positive", **parameters})
        if data["trace_preserving_residual"] > ABSOLUTE_TOLERANCE:
            violations.append({"check": "trace_preserving", **parameters})

        c_zero = omega * (-np.expm1(-2 * gamma * duration)) / (4 * gamma)
        residuals = {
            "population": data["p"] - omega**2 * duration**2 / 4,
            "c_squared": (
                abs(abs(data["c"]) ** 2 - c_zero**2)
                - omega**4 * duration**4 / 12
            ),
            "a_squared": (
                abs(abs(data["a"]) ** 2 - np.exp(-4 * gamma * duration))
                - omega**2 * duration**2 / 2
            ),
        }
        for name, residual in residuals.items():
            maximum_positive_bound_residuals[name] = max(
                maximum_positive_bound_residuals[name], float(residual)
            )
            if residual > ABSOLUTE_TOLERANCE:
                violations.append(
                    {"check": name, "residual": float(residual), **parameters}
                )

    return {
        "samples": samples,
        "parameter_ranges": {
            "omega": [0.01, 10.0],
            "gamma": [0.01, 10.0],
            "duration": [0.001, 10.0],
            "sampling": "independent log-uniform",
        },
        "maximum_identity_errors": maximum_errors,
        "maximum_positive_bound_residuals": maximum_positive_bound_residuals,
        "minimum_choi_eigenvalue": minimum_choi_eigenvalue,
        "maximum_trace_preserving_residual": maximum_trace_preserving_residual,
        "violations": violations,
    }


def check_partitions(rng: np.random.Generator, samples: int) -> dict:
    minimum_gaps = {
        "helstrom_minus_exact_genie_bound": float("inf"),
        "helstrom_minus_S_minus_2s_squared": float("inf"),
        "helstrom_minus_interval_replacement_bound": float("inf"),
    }
    violations = []

    for sample in range(samples):
        interval_count = int(rng.integers(1, 10))
        omega = 10 ** rng.uniform(-2, 0)
        gamma = 10 ** rng.uniform(-2, 1)
        durations = 10 ** rng.uniform(-2, 0.3, size=interval_count)
        data = [interval_data(omega, gamma, duration) for duration in durations]
        probabilities = np.array([entry["p"] for entry in data])
        c_squared = np.array([abs(entry["c"]) ** 2 for entry in data])
        a_squared = np.array([abs(entry["a"]) ** 2 for entry in data])
        stay = 1 - probabilities

        if np.any(probabilities <= 0) or np.any(stay <= 0):
            violations.append({"check": "nondegenerate_partition", "sample": sample})
            continue

        probability_zero = np.prod(stay)
        odds = probabilities / stay
        total_odds = np.sum(odds)
        helstrom = 0.0
        exact_genie_bound = 0.0
        sum_exact = 0.0
        sum_comparison = 0.0

        for index in range(interval_count):
            # These are joint weights, including the probability of this index
            # message. The high-change branch has zero error by construction.
            prior_zero = probability_zero * odds[index] / total_odds
            prior_one = probability_zero * odds[index]
            fidelity = (
                c_squared[index] / (probabilities[index] * stay[index])
                * np.prod(a_squared[index + 1 :] / stay[index + 1 :] ** 2)
            )
            if fidelity < -ABSOLUTE_TOLERANCE or fidelity > 1 + ABSOLUTE_TOLERANCE:
                violations.append(
                    {
                        "check": "normalized_field_overlap",
                        "sample": sample,
                        "fidelity": float(fidelity),
                    }
                )
            fidelity = float(np.clip(fidelity, 0, 1))
            total = prior_zero + prior_one
            discriminant = max(
                0.0, total**2 - 4 * prior_zero * prior_one * fidelity
            )
            # Rationalized form avoids subtracting nearly equal quantities.
            helstrom += (
                2 * prior_zero * prior_one * fidelity
                / (total + np.sqrt(discriminant))
            )
            exact_genie_bound += (
                probability_zero / (1 + total_odds)
                * c_squared[index] / stay[index] ** 2
                * np.prod(a_squared[index + 1 :] / stay[index + 1 :] ** 2)
            )
            sum_exact += c_squared[index] * np.prod(a_squared[index + 1 :])
            c_zero = (
                omega * (-np.expm1(-2 * gamma * durations[index])) / (4 * gamma)
            )
            sum_comparison += c_zero**2 * np.exp(
                -4 * gamma * np.sum(durations[index + 1 :])
            )

        sum_probabilities = np.sum(probabilities)
        values = {
            "helstrom_minus_exact_genie_bound": helstrom - exact_genie_bound,
            "helstrom_minus_S_minus_2s_squared": (
                helstrom - (sum_exact - 2 * sum_probabilities**2)
            ),
            "helstrom_minus_interval_replacement_bound": (
                helstrom
                - (sum_comparison - 5 * omega**4 * np.sum(durations**2) ** 2 / 24)
            ),
        }
        for name, gap in values.items():
            minimum_gaps[name] = min(minimum_gaps[name], float(gap))
            if gap < -ABSOLUTE_TOLERANCE:
                violations.append(
                    {"check": name, "sample": sample, "gap": float(gap)}
                )

    return {
        "samples": samples,
        "interval_counts": [1, 9],
        "minimum_lower_bound_gaps": minimum_gaps,
        "violations": violations,
    }


def check_renewal() -> dict:
    """Compare age-distribution quadrature with the exponential-sum formula."""
    total_rate = 1.0
    cases = []
    violations = []

    for gamma in (0.005, 0.1, 0.5):
        kappa = total_rate - gamma
        poisson_rate = 2 * kappa

        def reward(duration: float) -> float:
            return float((-np.expm1(-2 * gamma * duration)) ** 2)

        def terminal_reward(duration: float) -> float:
            density_part = quad(
                lambda age: poisson_rate * np.exp(-poisson_rate * age) * reward(age),
                0,
                duration,
                epsabs=1e-13,
            )[0]
            return float(
                np.exp(-poisson_rate * duration) * reward(duration) + density_part
            )

        for duration in (0.1, 2.0, 20.0):
            completed_reward = quad(
                lambda time: (
                    poisson_rate * terminal_reward(time)
                    * np.exp(-4 * gamma * (duration - time))
                ),
                0,
                duration,
                epsabs=1e-12,
            )[0]
            quadrature = terminal_reward(duration) + completed_reward
            if np.isclose(total_rate, 2 * gamma, rtol=0, atol=1e-14):
                cdf = 1 - (1 + 2 * total_rate * duration) * np.exp(
                    -2 * total_rate * duration
                )
            else:
                cdf = 1 - (
                    total_rate * np.exp(-4 * gamma * duration)
                    - 2 * gamma * np.exp(-2 * total_rate * duration)
                ) / (total_rate - 2 * gamma)
            formula = gamma / total_rate * cdf
            residual = float(abs(quadrature - formula))
            cases.append(
                {
                    "Gamma": total_rate,
                    "gamma": gamma,
                    "duration": duration,
                    "absolute_residual": residual,
                }
            )
            if residual > ABSOLUTE_TOLERANCE:
                violations.append({"check": "renewal_identity", **cases[-1]})

    return {
        "cases": cases,
        "maximum_absolute_residual": max(case["absolute_residual"] for case in cases),
        "violations": violations,
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--samples",
        type=int,
        default=250,
        help="sample count for each of the interval and partition checks (default: 250)",
    )
    parser.add_argument("--seed", type=int, default=574321)
    parser.add_argument(
        "--output",
        type=Path,
        help="optional JSON report path; the default writes only to standard output",
    )
    arguments = parser.parse_args()
    if arguments.samples < 1:
        parser.error("--samples must be positive")

    rng = np.random.default_rng(arguments.seed)
    interval_results = check_intervals(rng, arguments.samples)
    partition_results = check_partitions(rng, arguments.samples)
    renewal_results = check_renewal()
    violation_count = sum(
        len(results["violations"])
        for results in (interval_results, partition_results, renewal_results)
    )
    report = {
        "status": "passed" if violation_count == 0 else "failed",
        "scope": "finite numerical checks; not a proof of the uniform quantum converse",
        "seed": arguments.seed,
        "absolute_tolerance": ABSOLUTE_TOLERANCE,
        "versions": {"numpy": np.__version__, "scipy": scipy.__version__},
        "intervals": interval_results,
        "partitions": partition_results,
        "renewal": renewal_results,
        "violation_count": violation_count,
    }
    rendered = json.dumps(report, indent=2, allow_nan=False) + "\n"
    if arguments.output is not None:
        arguments.output.write_text(rendered, encoding="utf-8")
    print(rendered, end="")
    return 0 if violation_count == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
