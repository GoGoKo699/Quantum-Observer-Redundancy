#!/usr/bin/env python3
"""Check the counting receiver and the classical Wonham error numerically.

The stationary calculation constructs an independent 8-by-8 superoperator for
the two classical guess labels and their two-by-two qubit density matrices.
Random-state derivative checks test the correlation equations and invariance of
the unconditional source generator. Positive-integrand quadrature is compared
with the Bessel expression for the classical stationary filtering error.

These finite checks do not prove the homodyne comparison or the quantum converse.
See science/counting.md, science/imperfections.md, and science/homodyne.md.

Usage from the repository root:
    python verification/verify_tracking.py
    python verification/verify_tracking.py --output tracking_checks.json

Dependencies: NumPy and SciPy. No output file is written unless requested.
"""

from __future__ import annotations

import argparse
import json
from pathlib import Path

import numpy as np
import scipy
from scipy.integrate import quad
from scipy.special import kve


IDENTITY = np.eye(2, dtype=complex)
PAULI_X = np.array([[0, 1], [1, 0]], dtype=complex)
PAULI_Y = np.array([[0, -1j], [1j, 0]], dtype=complex)
PAULI_Z = np.diag([1, -1]).astype(complex)

MATRIX_TOLERANCE = 1e-10
DERIVATIVE_TOLERANCE = 1e-12
QUADRATURE_TOLERANCE = 1e-10

REAL_CASES = (
    (0.2, 1.0, 0.1, 1.0, 0.0, 0.0),
    (0.02, 1.0, 0.0005, 1.0, 0.0, 0.0),
    (2.0, 1.0, 0.8, 1.0, 0.0, 0.0),
    (0.0, 1.0, 0.2, 0.9, 0.0, 0.0),
    (0.0, 1.0, 0.2, 1.0, 0.03, 0.0),
    (0.3, 1.0, 0.15, 1.12, 0.01, 0.0),
)
PHASE_CASES = (
    (0.0, 1.0, 0.2, 1.0, 0.0, 0.17),
    (0.3, 1.0, 0.15, 1.12, 0.01, -0.35),
    (1.2, 1.0, 0.7, 0.8, 0.0, 0.9),
)


def dissipator(operator: np.ndarray, state: np.ndarray) -> np.ndarray:
    square = operator.conj().T @ operator
    return (
        operator @ state @ operator.conj().T
        - (square @ state + state @ square) / 2
    )


def augmented_action(
    blocks: np.ndarray,
    omega: float,
    total_rate: float,
    branch_rate: float,
    amplitude: float = 1.0,
    dark: float = 0.0,
    phase: float = 0.0,
) -> np.ndarray:
    """Apply the joint source/guess generator without using moment equations."""
    hamiltonian = omega * PAULI_X / 2
    beta = amplitude * np.exp(1j * phase)
    jumps = [
        np.sqrt(branch_rate) * (PAULI_Z - beta * guess * IDENTITY)
        for guess in (1, -1)
    ]
    output = []
    for index in range(2):
        state = blocks[index]
        jump = jumps[index]
        previous_jump = jumps[1 - index]
        derivative = -1j * (hamiltonian @ state - state @ hamiltonian)
        # Removing and rerouting the count term keeps the physical source
        # generator fixed. For complex beta this includes the displaced-
        # detection instrument correction; omitting it changes the source.
        derivative += total_rate * dissipator(PAULI_Z, state)
        derivative -= jump @ state @ jump.conj().T
        derivative += (
            previous_jump @ blocks[1 - index] @ previous_jump.conj().T
        )
        derivative += dark * (blocks[1 - index] - state)
        output.append(derivative)
    return np.stack(output)


def correlations(blocks: np.ndarray) -> tuple[float, float]:
    difference = blocks[0] - blocks[1]
    return tuple(
        float(np.trace(observable @ difference).real)
        for observable in (PAULI_Z, PAULI_Y)
    )


def matrix_stationary(parameters: tuple) -> np.ndarray:
    """Solve the augmented matrix equation with unconditional state I/2."""
    columns = []
    for index in range(8):
        basis = np.zeros(8, dtype=complex)
        basis[index] = 1
        columns.append(
            augmented_action(basis.reshape(2, 2, 2), *parameters).reshape(-1)
        )
    generator = np.stack(columns, axis=1)

    # At zero drive the source Z populations are conserved, so the stationary
    # kernel need not be one-dimensional. Specifying the unconditional state
    # resolves that degeneracy without assuming a unique stationary kernel.
    total_state_map = np.hstack([np.eye(4), np.eye(4)])
    equations = np.vstack([generator, total_state_map])
    right_hand_side = np.concatenate(
        [np.zeros(8), (IDENTITY / 2).reshape(-1)]
    )
    solution = np.linalg.lstsq(equations, right_hand_side, rcond=None)[0]
    return solution.reshape(2, 2, 2)


def formula_coefficients(parameters: tuple) -> tuple[complex, float, float]:
    _, total_rate, branch_rate, amplitude, dark, phase = parameters
    beta = amplitude * np.exp(1j * phase)
    k_y = 2 * (total_rate + branch_rate * (amplitude**2 - 1) + dark)
    k_z = 2 * branch_rate * (1 + amplitude**2) + 2 * dark
    return beta, k_y, k_z


def stationary_case(parameters: tuple) -> dict:
    omega, total_rate, branch_rate, amplitude, dark, phase = parameters
    blocks = matrix_stationary(parameters)
    correlation_z, correlation_y = correlations(blocks)
    beta, k_y, k_z = formula_coefficients(parameters)
    predicted_z = 4 * branch_rate * beta.real / (k_z + omega**2 / k_y)
    predicted_y = -omega * predicted_z / k_y
    return {
        "omega": omega,
        "Gamma": total_rate,
        "gamma": branch_rate,
        "amplitude": amplitude,
        "dark": dark,
        "phase": phase,
        "matrix_error": (1 - correlation_z) / 2,
        "formula_error": (1 - predicted_z) / 2,
        "stationary_residual": float(
            np.linalg.norm(augmented_action(blocks, *parameters))
        ),
        "correlation_residual": float(
            max(abs(correlation_z - predicted_z), abs(correlation_y - predicted_y))
        ),
        "unconditional_state_residual": float(
            np.linalg.norm(blocks[0] + blocks[1] - IDENTITY / 2)
        ),
        "hermiticity_residual": float(
            max(np.linalg.norm(block - block.conj().T) for block in blocks)
        ),
        "minimum_block_eigenvalue": float(
            min(
                np.linalg.eigvalsh((block + block.conj().T) / 2).min()
                for block in blocks
            )
        ),
    }


def random_derivative_checks(
    parameters_list: tuple, rng: np.random.Generator
) -> dict:
    maximum_correlation_residual = 0.0
    maximum_source_residual = 0.0
    trials = 0

    for parameters in parameters_list:
        omega, total_rate, branch_rate, _, _, _ = parameters
        beta, k_y, k_z = formula_coefficients(parameters)
        hamiltonian = omega * PAULI_X / 2
        for _ in range(10):
            factors = (
                rng.normal(size=(2, 2, 2))
                + 1j * rng.normal(size=(2, 2, 2))
            )
            blocks = np.stack(
                [factor @ factor.conj().T for factor in factors]
            )
            blocks /= np.trace(blocks[0] + blocks[1]).real
            state = blocks[0] + blocks[1]
            unconditional_x = float(np.trace(PAULI_X @ state).real)
            correlation_z, correlation_y = correlations(blocks)
            derivative = augmented_action(blocks, *parameters)
            derivative_z, derivative_y = correlations(derivative)
            predicted_z = (
                omega * correlation_y - k_z * correlation_z
                + 4 * branch_rate * beta.real
            )
            predicted_y = (
                -omega * correlation_z - k_y * correlation_y
                + 4 * branch_rate * beta.imag * unconditional_x
            )
            maximum_correlation_residual = max(
                maximum_correlation_residual,
                abs(derivative_z - predicted_z),
                abs(derivative_y - predicted_y),
            )
            source_derivative = (
                -1j * (hamiltonian @ state - state @ hamiltonian)
                + total_rate * dissipator(PAULI_Z, state)
            )
            maximum_source_residual = max(
                maximum_source_residual,
                float(
                    np.linalg.norm(
                        derivative[0] + derivative[1] - source_derivative
                    )
                ),
            )
            trials += 1

    return {
        "random_state_trials": trials,
        "maximum_correlation_derivative_residual": float(
            maximum_correlation_residual
        ),
        "maximum_unconditional_source_residual": float(maximum_source_residual),
    }


def wonham_bessel(q: float) -> float:
    """Classical stationary error using exponentially scaled Bessel functions."""
    return float((1 - 2 / (q * (kve(0, q / 2) + kve(1, q / 2)))) / 2)


def wonham_quadrature(q: float) -> float:
    """Evaluate the invariant-density error with positive integrands.

    The substitution z=tanh(x) and removal of a common exp(-q) factor give
    cosh(x)^2 exp[-q sinh(x)^2]. The upper endpoint corresponds to an exponent
    of -800. This is a finite numerical truncation, not an analytic tail proof.
    """

    def density(coordinate: float) -> float:
        cosine = np.cosh(coordinate)
        return float(
            cosine**2 * np.exp(-q * np.sinh(coordinate) ** 2)
        )

    upper = float(np.arcsinh(np.sqrt(800 / q)))
    normalizer = quad(
        density, 0, upper, epsabs=1e-10, epsrel=2e-12, limit=300
    )[0]
    numerator = quad(
        lambda coordinate: (
            (1 - np.tanh(coordinate)) * density(coordinate) / 2
        ),
        0,
        upper,
        epsabs=1e-12,
        epsrel=2e-12,
        limit=300,
    )[0]
    return float(numerator / normalizer)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--seed", type=int, default=817205)
    parser.add_argument(
        "--output",
        type=Path,
        help="optional JSON report path; default: standard output only",
    )
    arguments = parser.parse_args()
    rng = np.random.default_rng(arguments.seed)

    stationary_real = [stationary_case(parameters) for parameters in REAL_CASES]
    stationary_phase = [stationary_case(parameters) for parameters in PHASE_CASES]
    real_derivatives = random_derivative_checks(REAL_CASES, rng)
    phase_derivatives = random_derivative_checks(PHASE_CASES, rng)

    bessel_cases = []
    for q in (1e-5, 1e-3, 0.01, 0.1, 1.0, 10.0):
        bessel = wonham_bessel(q)
        quadrature = wonham_quadrature(q)
        leading = q * (np.log(4 / q) + 1 - np.euler_gamma) / 4
        bessel_cases.append(
            {
                "q": q,
                "bessel": bessel,
                "positive_integrand_quadrature": quadrature,
                "absolute_difference": abs(bessel - quadrature),
                "small_q_expression": float(leading),
                "ratio_to_small_q_expression": float(bessel / leading),
            }
        )

    violations = []

    def check_upper(name: str, value: float, tolerance: float) -> None:
        if not np.isfinite(value) or value > tolerance:
            violations.append(
                {"check": name, "value": value, "maximum_allowed": tolerance}
            )

    def check_lower(name: str, value: float, tolerance: float) -> None:
        if not np.isfinite(value) or value < -tolerance:
            violations.append(
                {"check": name, "value": value, "minimum_allowed": -tolerance}
            )

    for family, cases in (("real", stationary_real), ("phase", stationary_phase)):
        for index, case in enumerate(cases):
            for key in (
                "stationary_residual",
                "correlation_residual",
                "unconditional_state_residual",
                "hermiticity_residual",
            ):
                check_upper(f"{family}_{index}_{key}", case[key], MATRIX_TOLERANCE)
            check_lower(
                f"{family}_{index}_positive_blocks",
                case["minimum_block_eigenvalue"],
                MATRIX_TOLERANCE,
            )

    for family, results in (
        ("real", real_derivatives),
        ("phase", phase_derivatives),
    ):
        check_upper(
            f"{family}_correlation_derivatives",
            results["maximum_correlation_derivative_residual"],
            DERIVATIVE_TOLERANCE,
        )
        check_upper(
            f"{family}_unconditional_source",
            results["maximum_unconditional_source_residual"],
            DERIVATIVE_TOLERANCE,
        )

    for index, case in enumerate(bessel_cases):
        check_upper(
            f"bessel_quadrature_{index}",
            case["absolute_difference"],
            QUADRATURE_TOLERANCE,
        )

    report = {
        "status": "passed" if not violations else "failed",
        "scope": (
            "Finite augmented-generator, stationary-state, random-state derivative, "
            "source-invariance, and Bessel/quadrature checks"
        ),
        "limits": (
            "These checks do not prove the stochastic comparison or quantum "
            "converse. Small-q expressions are descriptive columns only and "
            "are not accuracy claims at large q."
        ),
        "seed": arguments.seed,
        "versions": {"numpy": np.__version__, "scipy": scipy.__version__},
        "tolerances": {
            "stationary_and_positivity": MATRIX_TOLERANCE,
            "derivatives_and_source_invariance": DERIVATIVE_TOLERANCE,
            "bessel_quadrature": QUADRATURE_TOLERANCE,
        },
        "real_stationary_cases": stationary_real,
        "phase_stationary_cases": stationary_phase,
        "real_random_derivatives": real_derivatives,
        "phase_random_derivatives": phase_derivatives,
        "bessel_cases": bessel_cases,
        "violations": violations,
    }
    rendered = json.dumps(report, indent=2, allow_nan=False) + "\n"
    if arguments.output is not None:
        arguments.output.write_text(rendered, encoding="utf-8")
    print(rendered, end="")
    return 0 if not violations else 1


if __name__ == "__main__":
    raise SystemExit(main())
