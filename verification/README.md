# Reproduction and finite verification

The analytical statements are proved in [the scientific account](../science/README.md). The scripts here check independently assembled finite matrix models, special-function evaluations, discrimination inequalities and generated examples. A passing numerical run does not prove a continuum-output theorem or optimize an arbitrary receiver.

## Environment and commands

The reference environment is Python 3.12.14 with NumPy 2.3.5, SciPy 1.17.0 and Matplotlib 3.10.8. Install the pinned dependencies from the repository root:

```bash
python -m pip install -r verification/requirements.txt
```

Run the two scientific check suites:

```bash
python verification/verify_tracking.py
python verification/verify_quantum_limit.py
```

Each prints a JSON report and returns a nonzero exit status if a check fails. To retain reports locally, use the optional output argument:

```bash
python verification/verify_tracking.py --output verification/results/tracking.json
python verification/verify_quantum_limit.py --output verification/results/quantum_limit.json
```

The output directory is excluded from version control. Neither script needs network access. Both use fixed random seeds for reproducible finite samples.

## What is checked

| Script | Independent construction | Coverage and limits |
|---|---|---|
| [verify_tracking.py](verify_tracking.py) | An eight-dimensional generator acting on two unnormalized qubit states; stationary solutions from linear algebra; direct derivatives on random positive states | Nine stationary parameter cases, 90 random-state derivative cases, complex-displacement source invariance, positivity and normalization, and six Bessel-versus-positive-quadrature comparisons. Checks the counting and imperfection algebra. |
| [verify_quantum_limit.py](verify_quantum_limit.py) | Interval channels from Liouville-space exponentiation, field overlaps reconstructed from Choi matrices, direct finite binary Helstrom errors, and Poisson-age quadrature | 250 interval cases, 250 finite partitions and nine renewal quadratures by default. Checks channel conventions, overlap identities, local remainders, unequal genie weights and the renewal coefficient. |
| [generate_comparison.py](generate_comparison.py) | Evaluation of the analytical counting formula and homodyne brackets; root finding with checked adjacent integer inequalities | Generates the two-panel figure and three finite observer-count examples. Illustrates proven bounds; it does not simulate a quantum trajectory or certify floating-point rounding by interval arithmetic. |

The augmented-generator calculation fixes the unconditional state to $`I/2`$ when finding stationary blocks. This also makes the zero-drive checks well defined, since the zero-drive source alone has conserved $`Z`$ populations. Random-state derivative checks independently test the correlation closure away from stationarity. Complex displacement is implemented with the source-preserving block generator, including the effect represented by the instrument Hamiltonian in a no-count formulation.

The quantum-limit script obtains a minimal Stinespring representation from the channel's Choi matrix. Its environment vectors reproduce the same overlaps as the actual interval output. This avoids a field time discretization. Only roundoff-level negative Choi eigenvalues may be removed; the minimum eigenvalue and trace-preservation residual are reported and checked. The finite-partition calculation retains the unequal prior weights supplied by the genie.

Reference runs with the pinned versions had no violations. The largest tracking correlation residual was approximately $`1.3\times10^{-13}`$, the largest random-state derivative residual was below $`9\times10^{-16}`$, and the Bessel/quadrature discrepancy was below $`10^{-16}`$. The quantum-limit overlap residual was below $`7\times10^{-15}`$ and its renewal residual below $`3\times10^{-16}`$. The reports contain the actual thresholds and individual diagnostics. Last digits may vary with numerical libraries and hardware.

## Regenerate the figure and observer-count examples

```bash
python verification/generate_comparison.py
```

This writes:

- [receiver_comparison.svg](../figures/receiver_comparison.svg): a vector figure with a fixed SVG hash salt and no date metadata.
- [comparison_values.json](../figures/comparison_values.json): parameter choices, versions, sampled values, root brackets, endpoint inequalities and the figure's SHA-256 digest.

The figure holds $`\eta=\gamma/\Gamma=10^{-4}`$ fixed and varies $`q`$ from $`10^{-6}`$ to $`10^{-1}`$, with $`r^2=2\eta q`$. The counting curve is exact for the specified receiver. The shaded homodyne band is

```math
e_{\mathrm W}(q)[1-T_{\mathrm{ad}}(r,\eta)]
\le e_{\mathrm H}^{\mathrm{opt}}
\le e_{\mathrm W}(q)[1+T(r,\eta)].
```

The dashed curve is the exact classical Wonham error. The plotted quantum homodyne quantity is a bracket, not a sampled or exactly evaluated optimum. The generator checks the assumptions and numerical ordering throughout the plotted grid. It uses exponentially scaled modified-Bessel functions on this finite range; no claim of arbitrarily small-$`q`$ floating-point accuracy is made.

The count table instead holds $`s=\Omega/\Gamma=10^{-4}`$ fixed and uses $`\eta=1/R`$. A count is attainable when the homodyne upper bound is at most the target, and is excluded when the lower bound exceeds it. Monotonicity of optimized receiver performance excludes all larger counts, without assuming global monotonicity of a bound expression. The script verifies the displayed integer and its neighbor on each side of the crossing. The nulling count is computed with decimal arithmetic before its endpoint error checks.

## What remains analytical

The tests do not establish the physical validity of the inaccessible-output instrument, its screening of arbitrary older quantum memory, the uniformity of the renewal remainder, or the arbitrary-policy homodyne inequality. Those require the respective proofs in [quantum_limit.md](../science/quantum_limit.md) and [homodyne.md](../science/homodyne.md). The homodyne comparison is analytical; no stochastic simulation is used to establish its asymptotic law.

The project also does not infer simultaneous independent observer errors, optimize imperfect receivers, or extrapolate the partial-output converse to complete collection. These distinctions are part of the [model](../science/model.md), [observer-count theorem](../science/observer_counts.md) and [imperfection analysis](../science/imperfections.md).
