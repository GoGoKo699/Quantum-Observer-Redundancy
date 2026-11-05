# A worked route from one guess to many observers

Imagine two observers watching separate output beams from the same driven qubit. Each maintains a sign guess. At a specified time, a projective Z measurement of the source supplies the outcome against which both guesses are scored. The beams are separate, but their records concern the same source and can be correlated.

The experiment charges one resource: the fixed total source coupling. Dividing the output gives each observer less information without changing the qubit's unconditional dynamics. The question is how the receiver operation affects the number of observers who can each meet a small error target.

This tutorial follows the settled [30-milestone map](milestones.md). Wiseman and Milburn's *Quantum Measurement and Control* (first edition, 2010) supplies the measurement and stochastic foundations; the [source bridge](source_bridge.md) connects its sections to the local derivations. The linked scientific pages contain the full hypotheses and proofs.

## 1. A state, a record and a prediction

**Milestones [M01–M04](milestones.md#m01).** Let $`Z`$ have eigenvalues $`+1`$ and $`-1`$, with projectors $`P_+`$ and $`P_-`$. For an observer's conditional state $`\rho`$, write $`z=\mathrm{tr}(Z\rho)`$. The better sign guess has conditional error

```math
h(z)=\frac{1-|z|}{2}.
```

The state used here depends on the available record. To see why that matters, consider an instantaneous joint source–bit state described by unnormalized blocks $`\rho_+`$ and $`\rho_-`$. Each block includes the probability of the stored guess. The following are admissible examples, not assertions about stationary states of the driven receiver.

| Source–bit blocks | Unconditional source state | Guess error |
|---|---|---|
| $`\rho_+=P_+/2,\quad\rho_-=P_-/2`$ | $`I/2`$ | Zero: the bit and the tested sign are perfectly correlated. |
| $`\rho_+=\rho_-=I/4`$ | $`I/2`$ | One half: the bit carries no information about the sign. |

The same unconditional state supports very different prediction performance. The relevant object is the correlation between the record, the guess and the source's terminal outcome.

The source Hamiltonian is $`H=\Omega X/2`$, and its dissipator is $`\Gamma\mathcal D[Z]`$. The dissipator alone makes off-diagonal source matrix elements decay at rate $`2\Gamma`$. Splitting the output into branches with couplings $`\gamma_1`$ and $`\gamma_2`$ satisfying $`\gamma_1+\gamma_2=\Gamma`$ leaves that total decay rate unchanged. The split changes access to the output, not the source generator. See the [model](../science/model.md).

## 2. A causal measurement record

**Milestones [M05–M11](milestones.md#m05).** A counting detector reports discrete events. A homodyne detector reports a noisy quadrature current. Each measurement is an instrument: it specifies both outcome probabilities and the corresponding conditional evolution. Forgetting its outcomes must reproduce the unconditional experiment that the model claims to describe.

The absence of a count also changes a conditional state. For a diffusive current, the innovation is the increment left after subtracting its conditional mean. A phase chosen from the past record is predictable: its setting is fixed before the next current increment arrives. These statements define which information a causal receiver may use.

The target measurement occurs at a fixed time or at a time sampled independently of the record. An observer cannot improve this task's score by asking to be tested only just after a favorable event. Long-run averaging is taken at fixed physical parameters before the asymptotic parameter limits.

The complete task combines that timing, the source dynamics, fixed output fractions, local receiver operations and a marginal error criterion. It supplies ideal local control and phase references; it does not charge total apparatus energy or bandwidth. This is the synthesis at [M11](milestones.md#m11).

## 3. One stored bit controls a counting receiver

**Milestones [M12–M13](milestones.md#m12).** Let the receiver's current guess be $`g=\pm1`$. A displacement makes its count operator

```math
J_g=\sqrt\gamma\,(Z-gI).
```

For a pointer eigenstate, the rate follows directly by squaring the corresponding amplitude:

| Pointer sign | Stored guess | Count rate | Action after a count |
|---|---|---|---|
| +1 | +1 | 0 | No count in this pointer-state case. |
| −1 | +1 | $`4\gamma`$ | Flip the guess to −1. |
| +1 | −1 | $`4\gamma`$ | Flip the guess to +1. |
| −1 | −1 | 0 | No count in this pointer-state case. |

A count projects onto the sign opposite to the old guess. Flipping the bit then makes it agree with that conditional source state. Between counts, the Hamiltonian continues to rotate the qubit. The table explains the local operation; it does not assign a classical sign trajectory to the source between events.

The exact error follows from the source–bit block equations. Define correlations $`c_z=\sum_g g\mathrm{tr}(Z\rho_g)`$ and $`c_y=\sum_g g\mathrm{tr}(Y\rho_g)`$. They satisfy

```math
\dot c_z=\Omega c_y+4\gamma(1-c_z),
\qquad
\dot c_y=-\Omega c_z-2\Gamma c_y.
```

At stationarity, eliminate $`c_y`$ and use the error $`(1-c_z)/2`$. With $`q=\Omega^2/(8\Gamma\gamma)`$, this gives

```math
e_{\mathrm{null}}=\frac{q}{2(1+q)}.
```

This is exact for the specified receiver. The [counting proof](../science/counting.md) derives the closure from the quantum instrument, so the calculation does not rely on a telegraph approximation.

## 4. A lower bound that includes quantum memory

**Milestones [M14–M19](milestones.md#m14).** An arbitrary observer could retain all previously received output in quantum memory. Comparing only a few familiar detectors cannot establish its best possible error.

The converse gives the observer extra information from a physical measurement of the inaccessible output. Splitting and displacing that lost output produces genuine rank-one pointer events at a state-independent Poisson rate. Averaging over this auxiliary record preserves the original source and observed-output experiment. Inserting an arbitrary measurement into the source's past would require a different argument because it could change that experiment.

When a genuine rank-one event is revealed, its source state is a known pointer state. Conditional on the event, it factorizes from older memory. Independent future input fields then allow the remaining problem to be expressed through intervals between events. Coherent source evolution inside each interval is retained exactly.

The proof supplies a further randomized message that leaves a controlled ambiguity between zero-change and one-change histories. Its weights are unequal. Binary quantum discrimination limits how well the corresponding pure field states can be distinguished. Bounds on each interval and Poisson averaging then control the accumulated remainder, including the final truncated interval.

For received fractions at most one half, the resulting leading lower bound matches the counting receiver as $`q\to0`$. This is what establishes asymptotic unrestricted optimality. Complete collection is a separate endpoint, and the one-query collective measurement available there does not automatically become a continuously reusable receiver. The [quantum-limit proof](../science/quantum_limit.md) makes both boundaries explicit.

## 5. Why the homodyne comparison must be relative

**Milestones [M20–M24](milestones.md#m20).** A classical two-state Wonham filter provides a useful reference error $`e_{\mathrm W}(q)`$. At small $`q`$,

```math
e_{\mathrm W}(q)\sim\frac q4\log\frac1q.
```

The reference is inherited classical filtering theory. To reach the quantum conclusion, the proof must compare it with the exact conditional qubit equations.

An absolute error estimate that merely tends to zero can be too weak: the tracking error itself also tends to zero. The proof therefore constructs a Poisson-equation solution for the loss $`h(z)`$ whose gradient is bounded by $`e_{\mathrm W}(q)`$ itself. This keeps the correction small on the scale of the quantity being estimated. Convexity controls the contribution from arbitrary predictable quadrature phase, while integrated moment bounds control the quantum transverse coordinates without assuming a stationary phase policy.

The result bounds every allowed homodyne policy from below and the real-quadrature receiver from above by relative factors approaching one as the drive ratio and received fraction vanish. Taking small $`q`$ then exposes the logarithm. Comparing the leading terms gives a homodyne-to-counting error ratio of approximately one half times $`\log(1/q)`$ in the common regime.

This statement concerns a diffusive quadrature current with classical processing and predictable phase. Finite-local-oscillator counting and general field preprocessing are different operations. The [homodyne proof](../science/homodyne.md) gives the finite bracket, its domain and the order of limits.

## 6. Turning an error law into an observer count

**Milestones [M25–M26](milestones.md#m25).** Suppose a fixed allocation serves $`R`$ observers. At least one branch has coupling no greater than $`\Gamma/R`$. An equal-share observer can discard excess information to emulate that weakest branch's actual successful receiver. Applying this construction to all equal branches proves equal-sharing feasibility without assuming that an abstract optimum is attained. In the homodyne case, the proof explicitly degrades the current while keeping the phase policy causal.

Write $`s=\Omega/\Gamma`$. Under equal sharing, $`q=s^2R/8`$. Inverting the exact counting formula at target error $`\epsilon<1/2`$ gives the attainable integer count

```math
R_{\mathrm{null}}
=\left\lfloor\frac{16\epsilon}{s^2(1-2\epsilon)}\right\rfloor.
```

The unrestricted converse and homodyne comparison give the optimal asymptotic counts

```math
R_{\mathrm Q}\sim\frac{16\epsilon}{s^2},
\qquad
R_{\mathrm H}\sim\frac{32\epsilon}{s^2\log(1/\epsilon)},
```

provided $`\epsilon\to0`$, $`s\to0`$ and $`s^2\log(1/\epsilon)=o(\epsilon)`$. The last condition makes both capacities diverge, so integer rounding does not change their leading terms. The proof uses attainable and excluded threshold counts, followed by monotonicity; it does not extend a local remainder estimate to arbitrarily large counts.

For a finite example, the supplied [comparison values](../figures/comparison_values.json) use $`s=10^{-4}`$ and $`\epsilon=10^{-3}`$. The explicit counting receiver supports **1,603,206** observers. Evaluating the homodyne inequalities gives an integer bracket from **333,694 to 334,989**. The first number comes from the exact constructive count formula; the bracket comes from finite-parameter analytical bounds evaluated in floating-point arithmetic, as explained in [verification](../verification/README.md). Neither should be relabeled as an exact finite-parameter unrestricted quantum optimum.

## 7. The ideal coefficient has an accuracy budget

**Milestones [M27–M28](milestones.md#m27).** The displacement and detector must become sufficiently accurate for the ideal asymptotic count to remain relevant. A complex displacement mismatch changes both the count operators and their no-count representation. The required Hamiltonian correction in that representation preserves the original source generator; it is not applied source feedback.

Two simple limits show the effect of imperfect operation for this particular click-and-flip policy. With a unit-amplitude displacement carrying phase error $`\phi`$, no drive and no dark counts, the stationary calibration floor is

```math
e_{\mathrm{phase}}=\sin^2(\phi/2)\sim\phi^2/4.
```

With ideal displacement, no drive and dark-click rate $`d`$, the floor is

```math
e_{\mathrm{dark}}=\frac{d}{2(2\gamma+d)}.
```

Reducing the drive alone does not remove either fixed floor. Detection loss instead reduces the received signal coupling. The [imperfection analysis](../science/imperfections.md) combines these effects in an exact stationary formula and accuracy inequality. Its scaling conditions identify when the ideal leading coefficient survives. These are guarantees and limitations of the specified receiver, not a universal impossibility theorem for every detector with noise.

## 8. What the complete argument establishes

**Milestones [M29–M30](milestones.md#m29).** The numerical checks independently construct finite generators, channel states, discrimination problems and quadratures. They can reveal convention, positivity, overlap and coefficient errors. The physical lost-output construction and the bound over every predictable phase remain analytical obligations, supplied by the proofs. The [verification account](../verification/README.md) and [related-work account](../references/related-work.md) separate these kinds of support and credit the inherited tools.

The combined conclusion is operational: a fixed quantum output can support parametrically more accurate causal guesses through displaced counting than through the defined diffusive homodyne class. At stringent tolerance, the ratio of their optimal observer counts grows as one half times the logarithm of the inverse tolerance, in the stated joint regime. Each observer meets its own marginal criterion. Correlations among observers, simultaneous unanimity, other access models and apparatus resource costs require their own questions and assumptions.
