#!/usr/bin/env python3
"""Generate the receiver-comparison figure and finite observer-count table.

The figure varies the drive at fixed received fraction eta=1e-4. Its Wonham
curve is the exact classical reference; the shaded region bounds the optimum
diffusive-homodyne error for the quantum source. It is not an exact quantum
homodyne curve.

The separate table fixes s=Omega/Gamma=1e-4 and varies the integer observer
count R. Every reported feasible/excluded integer has directly checked
endpoint inequalities. Exclusion of larger R uses monotonicity of the receiver
class, not an assumption that the analytic lower-bound expression is globally
monotone. All evaluations use ordinary floating-point numerics, not formal
interval arithmetic.

Run from any working directory:
    python verification/generate_comparison.py

Outputs:
    figures/receiver_comparison.svg
    figures/comparison_values.json
"""

from __future__ import annotations

from decimal import Decimal, ROUND_CEILING, localcontext
import hashlib
import json
from pathlib import Path
import platform

import matplotlib

matplotlib.use("Agg")

import matplotlib.pyplot as plt
from matplotlib.lines import Line2D
from matplotlib.patches import Patch
import numpy as np
import scipy
from scipy.optimize import brentq
from scipy.special import kve


Q_MIN = 1e-6
Q_MAX = 1e-1
SWEEP_ETA = 1e-4
SWEEP_POINTS = 501
TABLE_S_TEXT = "0.0001"
TABLE_EPSILON_TEXTS = ("0.0001", "0.001", "0.01")
SVG_HASHSALT = "quantum-observer-redundancy-receiver-comparison-v1"


def require(condition: bool, message: str) -> None:
    if not condition:
        raise ValueError(message)


def wonham_error(q):
    """Exact classical reference, evaluated only in the documented finite range."""
    q = np.asarray(q, dtype=float)
    require(bool(np.all(np.isfinite(q))), "Nonfinite Wonham parameter.")
    require(
        bool(np.all((q >= Q_MIN * (1 - 1e-12)) & (q <= Q_MAX * (1 + 1e-12)))),
        "Wonham evaluation lies outside the declared finite q range.",
    )
    result = (1 - 2 / (q * (kve(0, q / 2) + kve(1, q / 2)))) / 2
    require(
        bool(np.all(np.isfinite(result) & (result > 0) & (result < 0.5))),
        "Invalid Wonham evaluation.",
    )
    return result


def nulling_error(q):
    q = np.asarray(q, dtype=float)
    return q / (2 * (1 + q))


def homodyne_bounds(r_squared, eta) -> dict:
    """The exact-source comparison in science/homodyne.md."""
    r_squared = np.asarray(r_squared, dtype=float)
    eta = np.asarray(eta, dtype=float)
    a_coefficient = 1 - r_squared - eta
    b_coefficient = r_squared + 2 * eta
    c_coefficient = eta * (1 + eta / (1 - eta) ** 2)
    require(
        bool(np.all((eta > 0) & (eta < 1) & (r_squared > 0) & (a_coefficient > 0))),
        "The homodyne comparison requires 0<eta<1, r^2>0, and A>0.",
    )
    comparison_t = (
        b_coefficient + np.sqrt(b_coefficient**2 + 4 * a_coefficient * eta)
    ) / (2 * a_coefficient)
    adaptive_t = (
        b_coefficient
        + np.sqrt(b_coefficient**2 + 4 * a_coefficient * c_coefficient)
    ) / (2 * a_coefficient)
    q = r_squared / (2 * eta)
    reference = wonham_error(q)
    return {
        "q": q,
        "r_squared": r_squared,
        "eta": eta,
        "A": a_coefficient,
        "T": comparison_t,
        "T_ad": adaptive_t,
        "wonham": reference,
        "lower": reference * (1 - adaptive_t),
        "upper": reference * (1 + comparison_t),
    }


def bounds_at_count(observer_count: float, s: float) -> dict:
    values = homodyne_bounds(s**2 / 4, 1 / observer_count)
    return {name: float(value) for name, value in values.items()}


def crossing(
    component: str,
    epsilon: float,
    s: float,
    first_count: int,
    last_count: int,
) -> dict:
    """Find one bracketed crossing, without claiming global bound monotonicity."""

    def residual(observer_count: float) -> float:
        return bounds_at_count(observer_count, s)[component] - epsilon

    first_residual = residual(first_count)
    last_residual = residual(last_count)
    require(
        first_residual < 0 < last_residual,
        f"No verified sign-changing bracket for the {component} crossing.",
    )
    root, solver = brentq(
        residual,
        first_count,
        last_count,
        xtol=1e-7,
        rtol=1e-12,
        full_output=True,
        disp=True,
    )
    require(bool(solver.converged), f"The {component} root did not converge.")
    return {
        "root": float(root),
        "iterations": int(solver.iterations),
        "root_residual": residual(root),
        "bracket": [first_count, last_count],
        "bracket_residuals": [first_residual, last_residual],
    }


def feasible_integer(root: float, epsilon: float, s: float) -> int:
    candidate = int(np.floor(root))
    for _ in range(12):
        current = bounds_at_count(candidate, s)["upper"]
        following = bounds_at_count(candidate + 1, s)["upper"]
        if current <= epsilon < following:
            return candidate
        candidate += -1 if current > epsilon else 1
    raise ValueError("Could not verify adjacent integers around the upper crossing.")


def excluded_integer(root: float, epsilon: float, s: float) -> int:
    candidate = int(np.floor(root)) + 1
    for _ in range(12):
        previous = bounds_at_count(candidate - 1, s)["lower"]
        current = bounds_at_count(candidate, s)["lower"]
        if previous <= epsilon < current:
            return candidate
        candidate += 1 if current <= epsilon else -1
    raise ValueError("Could not verify adjacent integers around the lower crossing.")


def observer_count_table() -> list[dict]:
    rows = []
    s = float(TABLE_S_TEXT)
    with localcontext() as context:
        context.prec = 50
        s_decimal = Decimal(TABLE_S_TEXT)
        first_count = int(
            (
                Decimal(8) * Decimal("0.000001") / s_decimal**2
            ).to_integral_value(rounding=ROUND_CEILING)
        )
        for epsilon_text in TABLE_EPSILON_TEXTS:
            epsilon_decimal = Decimal(epsilon_text)
            epsilon = float(epsilon_text)
            nulling_boundary = (
                16 * epsilon_decimal
                / (s_decimal**2 * (1 - 2 * epsilon_decimal))
            )
            nulling_count = int(nulling_boundary)

            upper_crossing = crossing(
                "upper", epsilon, s, first_count, nulling_count
            )
            lower_crossing = crossing(
                "lower", epsilon, s, first_count, nulling_count
            )
            feasible_count = feasible_integer(
                upper_crossing["root"], epsilon, s
            )
            excluded_count = excluded_integer(
                lower_crossing["root"], epsilon, s
            )
            require(
                first_count <= feasible_count < excluded_count <= nulling_count,
                "The evaluated observer counts have an unexpected order.",
            )

            upper_at_feasible = bounds_at_count(feasible_count, s)["upper"]
            upper_at_next = bounds_at_count(feasible_count + 1, s)["upper"]
            lower_at_previous = bounds_at_count(excluded_count - 1, s)["lower"]
            lower_at_excluded = bounds_at_count(excluded_count, s)["lower"]
            null_error_at_count = float(nulling_error(s**2 * nulling_count / 8))
            null_error_at_next = float(nulling_error(s**2 * (nulling_count + 1) / 8))
            require(
                null_error_at_count <= epsilon < null_error_at_next,
                "The exact nulling-count floor failed its endpoint check.",
            )

            rows.append(
                {
                    "s": s,
                    "epsilon": epsilon,
                    "nulling_maximum_integer_R": nulling_count,
                    "nulling_real_boundary_decimal": str(nulling_boundary),
                    "homodyne_feasible_integer_R": feasible_count,
                    "homodyne_first_excluded_integer_at_crossing": excluded_count,
                    "homodyne_maximum_R_bracket": [
                        feasible_count, excluded_count - 1
                    ],
                    "upper_crossing": upper_crossing,
                    "lower_crossing": lower_crossing,
                    "endpoint_checks": {
                        "nulling_error_at_R_null": null_error_at_count,
                        "nulling_error_at_R_null_plus_1": null_error_at_next,
                        "homodyne_upper_at_feasible_R": upper_at_feasible,
                        "homodyne_upper_at_feasible_R_plus_1": upper_at_next,
                        "homodyne_lower_at_excluded_R_minus_1": lower_at_previous,
                        "homodyne_lower_at_excluded_R": lower_at_excluded,
                        "feasible_margin": epsilon - upper_at_feasible,
                        "excluded_margin": lower_at_excluded - epsilon,
                        "all_requested_inequalities_checked": True,
                    },
                }
            )
    return rows


def make_figure(path: Path, q: np.ndarray, values: dict) -> None:
    null_error = nulling_error(q)
    reference = values["wonham"]
    lower = values["lower"]
    upper = values["upper"]
    null_color = "#17436C"
    reference_color = "#BC5A16"
    bound_color = "#7253B5"

    with plt.rc_context(
        {
            "font.family": "DejaVu Sans",
            "font.size": 10,
            "axes.labelsize": 11,
            "axes.titlesize": 12,
            "axes.spines.top": False,
            "axes.spines.right": False,
            "svg.fonttype": "none",
            "svg.hashsalt": SVG_HASHSALT,
            "savefig.facecolor": "white",
        }
    ):
        figure, axes = plt.subplots(1, 2, figsize=(12.6, 5.3))
        figure.subplots_adjust(
            left=0.075, right=0.98, bottom=0.27, top=0.77, wspace=0.28
        )

        for axis in axes:
            axis.set_xscale("log")
            axis.set_xlim(Q_MIN, Q_MAX)
            axis.set_xlabel(r"$q=\Omega^2/(8\Gamma\gamma)$")
            axis.grid(which="major", alpha=0.22, linewidth=0.6)
            axis.tick_params(which="both", direction="out")

        axes[0].set_yscale("log")
        axes[0].fill_between(q, lower, upper, color=bound_color, alpha=0.36)
        axes[0].plot(q, lower, color=bound_color, linewidth=0.9)
        axes[0].plot(q, upper, color=bound_color, linewidth=0.9)
        axes[0].plot(q, reference, color=reference_color, linestyle="--", linewidth=1.3)
        axes[0].plot(q, null_error, color=null_color, linewidth=2.0)
        axes[0].set_ylim(3.0e-7, 0.13)
        axes[0].set_ylabel("Stationary / long-run prediction error")
        axes[0].set_title("(a) Absolute error", loc="left", pad=10)

        axes[1].fill_between(
            q, lower / null_error, upper / null_error,
            color=bound_color, alpha=0.36,
        )
        axes[1].plot(q, lower / null_error, color=bound_color, linewidth=0.9)
        axes[1].plot(q, upper / null_error, color=bound_color, linewidth=0.9)
        axes[1].plot(
            q, reference / null_error,
            color=reference_color, linestyle="--", linewidth=1.3,
        )
        axes[1].axhline(1, color=null_color, linewidth=2.0)
        axes[1].set_ylim(0.7, 8.4)
        axes[1].set_yticks(np.arange(1, 9))
        axes[1].set_ylabel(r"Error divided by $e_{\mathrm{null}}$")
        axes[1].set_title("(b) Penalty relative to ideal nulling", loc="left", pad=10)
        axes[1].annotate(
            "Analytic homodyne bounds",
            xy=(4e-5, float(np.interp(np.log10(4e-5), np.log10(q), upper / null_error))),
            xytext=(2.4e-4, 7.0),
            color=bound_color,
            fontsize=9.5,
            arrowprops={"arrowstyle": "->", "color": bound_color, "linewidth": 0.9},
        )

        figure.suptitle("Receiver error and the homodyne penalty", y=0.98, fontsize=17)
        figure.text(
            0.5,
            0.91,
            r"Drive sweep at fixed $\eta=\gamma/\Gamma=10^{-4}$: "
            r"$r^2=2\eta q$; equal sharing has fixed $R=10^4$",
            ha="center",
            fontsize=11,
        )
        handles = [
            Line2D([0], [0], color=null_color, linewidth=2.0),
            Line2D([0], [0], color=reference_color, linestyle="--", linewidth=1.3),
            Patch(facecolor=bound_color, edgecolor=bound_color, alpha=0.36),
        ]
        labels = [
            "Ideal nulling (exact quantum error)",
            "Exact classical Wonham reference",
            "Exact-source diffusive-homodyne bounds",
        ]
        figure.legend(
            handles,
            labels,
            loc="lower center",
            bbox_to_anchor=(0.5, 0.105),
            ncol=3,
            frameon=False,
            fontsize=9.5,
            handlelength=2.4,
            columnspacing=1.5,
        )
        figure.text(
            0.5,
            0.055,
            r"Shaded band: "
            r"$e_{\mathrm{W}}(q)(1-T_{\mathrm{ad}})"
            r"\leq e_{\mathrm{H}}^{\mathrm{opt}}"
            r"\leq e_{\mathrm{W}}(q)(1+T)$",
            ha="center",
            fontsize=10.5,
        )
        figure.savefig(
            path,
            format="svg",
            metadata={
                "Title": "Receiver error and the homodyne penalty",
                "Description": (
                    "Drive varied at fixed received fraction eta=0.0001. "
                    "Ideal quantum nulling and the exact classical Wonham "
                    "reference are compared with analytic bounds on optimal "
                    "diffusive homodyne for the driven quantum source."
                ),
                "Creator": "verification/generate_comparison.py",
                "Date": None,
            },
        )
        plt.close(figure)


def main() -> int:
    repository = Path(__file__).resolve().parents[1]
    figure_directory = repository / "figures"
    figure_directory.mkdir(parents=True, exist_ok=True)
    figure_path = figure_directory / "receiver_comparison.svg"
    values_path = figure_directory / "comparison_values.json"

    q = np.logspace(np.log10(Q_MIN), np.log10(Q_MAX), SWEEP_POINTS)
    values = homodyne_bounds(2 * SWEEP_ETA * q, SWEEP_ETA)
    null_error = nulling_error(q)
    require(
        bool(np.all(
            (values["lower"] > 0)
            & (values["lower"] <= values["wonham"])
            & (values["wonham"] <= values["upper"])
            & (null_error < values["lower"])
        )),
        "The plotted bounds or their ordering failed a finite numerical check.",
    )
    table = observer_count_table()
    make_figure(figure_path, q, values)
    figure_hash = hashlib.sha256(figure_path.read_bytes()).hexdigest()
    sample_rows = []
    for index in range(0, SWEEP_POINTS, 100):
        sample_rows.append(
            {
                "q": float(q[index]),
                "r_squared": float(values["r_squared"][index]),
                "nulling_error": float(null_error[index]),
                "classical_wonham_error": float(values["wonham"][index]),
                "homodyne_lower_bound": float(values["lower"][index]),
                "homodyne_upper_bound": float(values["upper"][index]),
                "ratio_lower": float(values["lower"][index] / null_error[index]),
                "ratio_upper": float(values["upper"][index] / null_error[index]),
            }
        )

    report = {
        "status": "passed",
        "evaluation_type": (
            "Ordinary floating-point numerical evaluation with checked endpoint "
            "inequalities; not formal interval certification"
        ),
        "versions": {
            "python": platform.python_version(),
            "numpy": np.__version__,
            "scipy": scipy.__version__,
            "matplotlib": matplotlib.__version__,
        },
        "figure": {
            "path": "figures/receiver_comparison.svg",
            "sha256": figure_hash,
            "svg_hashsalt": SVG_HASHSALT,
            "svg_date_metadata": None,
        },
        "drive_sweep": {
            "eta": SWEEP_ETA,
            "equal_sharing_R": 10000,
            "q_range": [Q_MIN, Q_MAX],
            "points": SWEEP_POINTS,
            "relationship": "r_squared=2*eta*q; drive varies while eta is fixed",
            "wonham_role": "exact classical reference, not exact quantum homodyne",
            "shaded_quantity": (
                "analytic bracket for exact-source optimal diffusive homodyne"
            ),
            "minimum_A": float(np.min(values["A"])),
            "T_range": [float(np.min(values["T"])), float(np.max(values["T"]))],
            "T_ad_range": [
                float(np.min(values["T_ad"])), float(np.max(values["T_ad"]))
            ],
            "minimum_lower_bound_to_nulling_ratio": float(
                np.min(values["lower"] / null_error)
            ),
            "sample_values": sample_rows,
        },
        "observer_count_interpretation": {
            "fixed_s": float(TABLE_S_TEXT),
            "access": "equal sharing, eta=1/R, q=s^2*R/8",
            "nulling": (
                "Exact integer floor of 16*epsilon/[s^2*(1-2*epsilon)], "
                "also checked at that count and the next integer"
            ),
            "feasible": (
                "The upper homodyne bound is at most epsilon at the listed "
                "feasible count; the real quadrature attains this guarantee."
            ),
            "excluded": (
                "The lower homodyne bound exceeds epsilon at the listed "
                "excluded count. All larger counts are excluded because the "
                "optimal receiver-class error is nondecreasing as received "
                "fraction decreases. No global monotonicity of the bound "
                "expression is assumed."
            ),
            "maximum_count_bracket": (
                "The optimal homodyne count lies between the feasible count "
                "and one less than the excluded count, inclusively."
            ),
            "roots": (
                "Each root has a sign-changing continuous bracket and checked "
                "adjacent integer inequalities; a root is a numerical evaluation."
            ),
        },
        "observer_counts": table,
    }
    values_path.write_text(
        json.dumps(report, indent=2, allow_nan=False) + "\n", encoding="utf-8"
    )
    print(
        json.dumps(
            {
                "status": report["status"],
                "figure_sha256": figure_hash,
                "versions": report["versions"],
                "minimum_plotted_homodyne_lower_to_nulling_ratio": (
                    report["drive_sweep"]["minimum_lower_bound_to_nulling_ratio"]
                ),
                "observer_counts": [
                    {
                        "epsilon": row["epsilon"],
                        "R_null": row["nulling_maximum_integer_R"],
                        "R_hom_feasible": row["homodyne_feasible_integer_R"],
                        "R_hom_excluded": row[
                            "homodyne_first_excluded_integer_at_crossing"
                        ],
                        "feasible_margin": row["endpoint_checks"]["feasible_margin"],
                        "excluded_margin": row["endpoint_checks"]["excluded_margin"],
                    }
                    for row in table
                ],
            },
            indent=2,
            allow_nan=False,
        )
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
