#!/usr/bin/env python3
"""Check the exact joint law of the simultaneous displaced-counting receivers.

This check assembles the quantum source and all classical guess sectors using
matrix jump operators. It compares the stationary distribution with the subset
recursion and the equal-split beta-binomial formula.

Usage from the repository root:
    python verification/verify_unanimity.py
    python verification/verify_unanimity.py --output unanimity_checks.json

Dependency: NumPy. No output file is written unless requested.
"""

from __future__ import annotations

import argparse
from itertools import product
import json
from math import comb, prod
from pathlib import Path

import numpy as np


IDENTITY = np.eye(2, dtype=complex)
PAULI_X = np.array([[0, 1], [1, 0]], dtype=complex)
PAULI_Z = np.diag([1, -1]).astype(complex)
TOLERANCE = 1e-10


def augmented_generator(
    omega: float, total_rate: float, branches: tuple[float, ...]
) -> np.ndarray:
    """Build the full hybrid generator from the no-count and count maps."""
    sector_count = 2 ** len(branches)
    hamiltonian = omega * PAULI_X / 2
    lost_rate = total_rate - sum(branches)
    generator = np.zeros((4 * sector_count, 4 * sector_count), dtype=complex)
    matrix_units = np.eye(4, dtype=complex).reshape(4, 2, 2)

    for sector in range(sector_count):
        start = 4 * sector
        jumps = [
            np.sqrt(branch) * (PAULI_Z - (-1 if sector & (1 << i) else 1) * IDENTITY)
            for i, branch in enumerate(branches)
        ]
        intensity = sum(jump.conj().T @ jump for jump in jumps)

        for coordinate, matrix in enumerate(matrix_units):
            column = start + coordinate
            no_count = -1j * (hamiltonian @ matrix - matrix @ hamiltonian)
            no_count += lost_rate * (PAULI_Z @ matrix @ PAULI_Z - matrix)
            no_count -= (intensity @ matrix + matrix @ intensity) / 2
            generator[start : start + 4, column] = no_count.reshape(-1)

            for index, jump in enumerate(jumps):
                target = 4 * (sector ^ (1 << index))
                received_count = jump @ matrix @ jump.conj().T
                generator[target : target + 4, column] = received_count.reshape(-1)

    return generator


def stationary_blocks(
    generator: np.ndarray,
) -> tuple[np.ndarray, dict[str, float]]:
    """Solve with the physical unconditional stationary source state."""
    sector_count = generator.shape[0] // 4
    source_sum = np.tile(np.eye(4), (1, sector_count))
    equations = np.vstack((generator, source_sum))
    rhs = np.concatenate((np.zeros(len(generator)), (IDENTITY / 2).reshape(-1)))
    solution = np.linalg.lstsq(equations, rhs, rcond=None)[0]
    blocks = solution.reshape(sector_count, 2, 2)
    adjoints = blocks.conj().transpose(0, 2, 1)
    diagnostics = {
        "stationary_residual": float(np.max(np.abs(generator @ solution))),
        "unconditional_state_residual": float(
            np.max(np.abs(source_sum @ solution - (IDENTITY / 2).reshape(-1)))
        ),
        "hermiticity_residual": float(np.max(np.abs(blocks - adjoints))),
        "minimum_block_eigenvalue": float(
            np.min(np.linalg.eigvalsh((blocks + adjoints) / 2))
        ),
    }
    return blocks, diagnostics


def exact_wrong_set_probabilities(blocks: np.ndarray) -> np.ndarray:
    """Compute probabilities of the complete mismatch pattern."""
    sector_count = len(blocks)
    sign_mask = sector_count - 1
    probabilities = np.zeros(sector_count)
    for sector, state in enumerate(blocks):
        probabilities[sector] += state[0, 0].real
        probabilities[sector ^ sign_mask] += state[1, 1].real
    return probabilities


def subset_probabilities(
    omega: float, total_rate: float, branches: tuple[float, ...]
) -> np.ndarray:
    """Evaluate the proposed all-correct probabilities for every subset."""
    flip_rates = tuple(4 * branch for branch in branches)
    switching_scale = omega**2 / (4 * total_rate)
    all_correct = np.ones(2 ** len(branches))
    for mask in range(1, len(all_correct)):
        indices = [i for i in range(len(branches)) if mask & (1 << i)]
        rate_sum = sum(flip_rates[i] for i in indices)
        weighted_previous = sum(
            flip_rates[i] * all_correct[mask ^ (1 << i)] for i in indices
        )
        all_correct[mask] = (
            (rate_sum + switching_scale)
            / (rate_sum + 2 * switching_scale)
            * weighted_previous
            / rate_sum
        )
    return all_correct


def wrong_set_probabilities(all_correct: np.ndarray) -> np.ndarray:
    """Invert the subset probabilities by inclusion and exclusion."""
    full_mask = len(all_correct) - 1
    probabilities = np.zeros(len(all_correct))
    for wrong in range(len(all_correct)):
        correct = full_mask ^ wrong
        include = wrong
        while True:
            probabilities[wrong] += (-1) ** include.bit_count() * all_correct[
                correct | include
            ]
            if include == 0:
                break
            include = (include - 1) & wrong
    return probabilities


def beta_binomial_probabilities(
    count: int, omega: float, total_rate: float, branch: float
) -> np.ndarray:
    """Evaluate the probability of each error count for equal branches."""
    shape = omega**2 / (16 * total_rate * branch)
    denominator = prod(1 + 2 * shape + offset for offset in range(count))
    return np.array(
        [
            comb(count, errors)
            * prod(shape + offset for offset in range(errors))
            * prod(1 + shape + offset for offset in range(count - errors))
            / denominator
            for errors in range(count + 1)
        ]
    )


def stationary_cases() -> list[dict]:
    records = []
    allocations = (
        (0.2,),
        (1.0,),
        (0.35, 0.65),
        (0.27, 0.27),
        (0.2, 0.3, 0.5),
        (0.19, 0.19, 0.19),
        (0.01, 0.03, 0.21, 0.4),
        (0.25, 0.25, 0.25, 0.25),
        (0.16, 0.16, 0.16, 0.16, 0.16),
    )
    parameters = product(((0.17, 0.7), (0.8, 1.0), (2.1, 1.3)), allocations)
    for (omega, total_rate), fractions in parameters:
        branches = tuple(total_rate * fraction for fraction in fractions)
        generator = augmented_generator(omega, total_rate, branches)
        blocks, diagnostics = stationary_blocks(generator)
        observed = exact_wrong_set_probabilities(blocks)
        all_correct = subset_probabilities(omega, total_rate, branches)
        predicted = wrong_set_probabilities(all_correct)
        records.append(
            {
                "omega": omega,
                "total_rate": total_rate,
                "branches": branches,
                "stationary_all_correct": float(observed[0]),
                "formula_all_correct": float(all_correct[-1]),
                "wrong_set_law_residual": float(np.max(np.abs(observed - predicted))),
                "normalization_residual": float(abs(sum(observed) - 1)),
                **diagnostics,
            }
        )
        if len(set(branches)) == 1:
            weight = [mask.bit_count() for mask in range(len(observed))]
            observed_count = np.bincount(weight, weights=observed)
            predicted_count = beta_binomial_probabilities(
                len(branches), omega, total_rate, branches[0]
            )
            records[-1]["beta_binomial_residual"] = float(
                np.max(np.abs(observed_count - predicted_count))
            )
    return records


def equal_allocation_checks() -> dict[str, float | int]:
    """Compare the equal allocation with deterministic unequal splits."""
    rng = np.random.default_rng(1117)
    gaps = []
    for count, omega, concentration in product(
        (2, 3, 4, 6), (0.1, 0.7, 2.0), (0.2, 1, 10)
    ):
        equal = (1 / count,) * count
        equal_value = subset_probabilities(omega, 1, equal)[-1]
        for unequal in rng.dirichlet([concentration] * count, size=12):
            unequal_value = subset_probabilities(omega, 1, tuple(unequal))[-1]
            gaps.append(equal_value - unequal_value)
    return {"comparisons": len(gaps), "minimum_equal_minus_unequal": float(min(gaps))}


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path)
    arguments = parser.parse_args()

    cases = stationary_cases()
    failures = []
    for index, case in enumerate(cases):
        for key, value in case.items():
            if key.endswith("_residual"):
                if not np.isfinite(value) or value > TOLERANCE:
                    failures.append({"case": index, "check": key, "value": value})
        minimum_eigenvalue = case["minimum_block_eigenvalue"]
        if not np.isfinite(minimum_eigenvalue) or minimum_eigenvalue < -TOLERANCE:
            failures.append(
                {"case": index, "check": "positive_blocks", "value": minimum_eigenvalue}
            )

    allocations = equal_allocation_checks()
    gap = allocations["minimum_equal_minus_unequal"]
    if not np.isfinite(gap) or gap < -TOLERANCE:
        failures.append({"check": "equal_allocation", "value": gap})
    report = {
        "status": "failed" if failures else "passed",
        "scope": "Finite hybrid-generator, full stationary law, and allocation checks",
        "numpy_version": np.__version__,
        "tolerance": TOLERANCE,
        "stationary_cases": cases,
        "equal_allocation": allocations,
        "violations": failures,
    }
    rendered = json.dumps(report, indent=2, allow_nan=False) + "\n"
    if arguments.output is not None:
        arguments.output.write_text(rendered, encoding="utf-8")
    print(rendered, end="")
    return int(bool(failures))


if __name__ == "__main__":
    raise SystemExit(main())
