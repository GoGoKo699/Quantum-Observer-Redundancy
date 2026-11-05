# A shared quantum source and a causal guessing task

How many observers can independently maintain an accurate guess of the same changing quantum observable when they share a fixed output field? The answer depends on what each observer measures. This repository compares a simple displaced-counting receiver with the best diffusive homodyne receiver, and bounds both against arbitrary quantum processing of each observer's output.

The task is deliberately operational. At a chosen time, each observer supplies a bit and the source is measured in the same basis. The error is the probability that a bit disagrees with that measurement. No unobserved classical trajectory is assigned to the source.

## 1. Source and output sharing

Let $`X,Y,Z`$ be the Pauli operators, with $`Z|\pm\rangle=\pm|\pm\rangle`$. A driven qubit obeys

```math
\frac{d\rho}{dt}=\mathcal L\rho,
\qquad
\mathcal L\rho=-i[\Omega X/2,\rho]+\Gamma\mathcal D[Z]\rho,
```

where

```math
\mathcal D[L]\rho=L\rho L^\dagger-\frac12\{L^\dagger L,\rho\},
\qquad \Gamma>0,\quad\Omega>0.
```

In this convention, an off-diagonal matrix element decays at rate $`2\Gamma`$ when the drive is absent. The vacuum Markov output coupling is $`\sqrt\Gamma Z`$. The standard input–output and quantum-filtering framework is described in the [continuous-measurement references](../references/related-work.md#continuous-quantum-measurement).

A passive splitter, with vacuum in its unused input ports, gives observer $`i`$ a fixed branch of coupling $`\sqrt{\gamma_i}Z`$. Unreceived output has total coupling strength $`\Gamma-\sum_i\gamma_i`$. Thus

```math
\gamma_i>0,
\qquad \sum_{i=1}^R\gamma_i\le\Gamma.
```

Every allocation leaves the source generator unchanged. For one observer with branch strength $`\gamma`$, all other branches are inaccessible and together contribute $`(\Gamma-\gamma)\mathcal D[Z]`$ to the reduced dynamics.

The fractions are fixed in time. Observers do not communicate or share detector records. All receiver operations occur downstream, with no Hamiltonian or measurement feedback to the source. Receivers may use independent local ancillary systems and randomization. A known optical phase reference is supplied.

## 2. What an observer must predict

A causal receiver $`\pi`$ processes its output up to time $`t`$ and supplies a classical guess $`g_\pi(t)\in\{-1,+1\}`$. Let $`Z_t^{\mathrm{test}}`$ denote the outcome of a projective measurement of the source's $`Z`$ observable at that time. Define

```math
e_\pi(t)=\Pr\{g_\pi(t)\ne Z_t^{\mathrm{test}}\},
\qquad
\overline e_\pi=
\limsup_{T\to\infty}\frac1T\int_0^T e_\pi(t)\,dt.
```

Each value $`e_\pi(t)`$ refers to the experiment stopped and tested at that time. The integral does not insert repeated projective measurements of the source into a single run. Equivalently, one can sample a test time uniformly in a long operating interval. A fixed causal receiver runs throughout that interval.

Earlier output observables commute with the terminal source observable. This gives a joint probability distribution for all observers' guesses and the one terminal test. An observer with a classical record and conditional source state $`\rho_t`$ minimizes its error by taking the sign of $`z_t=\operatorname{Tr}(Z\rho_t)`$. Its conditional error is

```math
h(z_t)=\frac{1-|z_t|}{2}.
```

The long-time limit is taken at each fixed positive parameter triple before any weak-drive or many-observer limit. The source's unconditional stationary state is $`I/2`$ for $`\Omega>0`$. The bounds below allow arbitrary initial source states; their transient contributions vanish in the long-run criterion.

## 3. Receiver classes

| Class | Allowed operation on one branch | Error addressed here |
|---|---|---|
| Displaced counting | Displace the output according to one stored bit, count photons, flip the bit after a click | Exact stationary error of this explicit receiver |
| Diffusive homodyne with adaptive phase | Measure a quadrature current; choose its phase predictably from the complete past classical record; process that record causally | Infimum of the long-run mean error over this class |
| Arbitrary quantum receiver | Any causal quantum instrument, private quantum memory, local ancillas and classical output decisions | Infimum over the larger class, bounded through a terminal collective-measurement relaxation |

The homodyne class is the quadrature-current diffusion written explicitly in [the homodyne analysis](homodyne.md). It is not a claim about all Gaussian receivers. The class includes arbitrary classical memory and independent classical randomness. A receiver can discard information or add independent current noise, so receiving a stronger branch cannot worsen its optimized error.

In the [quantum converse](quantum_limit.md), the observer is granted the entire unmeasured past field and an arbitrary collective measurement at the test time. This is at least as powerful as continuously processing that field and maintaining a classical guess. A lower bound for the granted experiment therefore bounds the operational receivers above. The relaxation does not assert that the same stored field can be consumed repeatedly at many times.

Earlier papers sometimes use the phrase “adaptive homodyne” for photon counting after a finite local-oscillator displacement. That operation belongs to the displaced-photon-counting measurement family. The [related-work account](../references/related-work.md#continuous-quantum-measurement) keeps these measurement classes separate.

## 4. The resource and the observer count

For $`\mathcal C\in\{\mathrm Q,\mathrm H\}`$, let

```math
e_{\mathcal C}(\Gamma,\Omega,\gamma)
=\inf_{\pi\in\mathcal C}\overline e_\pi.
```

For a target $`0<\epsilon<1/2`$, define $`R_{\mathcal C}(\epsilon;\Gamma,\Omega)`$ as the largest number of observers for which fixed fractions and receivers in class $`\mathcal C`$ give every observer $`\overline e_i\le\epsilon`$. When no positive number is feasible, the count is zero. The [observer-count analysis](observer_counts.md) treats attainable constructions and upper bounds separately, so no unattained infimum is presumed to be a receiver.

The charged shared resource is $`\Gamma`$, the total coupling to the source. Both receiver classes see the same drive $`\Omega`$ and the same total output. The comparison does not charge local-oscillator power, phase stabilization, detector bandwidth, controller speed or memory. The ideal counting law assumes unit detector efficiency, zero dark counts and instantaneous local displacement changes. [Imperfections](imperfections.md) quantifies calibration, efficiency and dark-count effects for the explicit receiver.

The criterion controls each observer's marginal error. If two observers each have error at most $`\epsilon`$ at a given time, their disagreement probability is at most $`2\epsilon`$, by the union bound. The corresponding statement holds for long-run means. There is no independence assumption, and a growing number of individually accurate guesses does not by itself imply that all guesses agree with high probability. The elementary all-observer bound is only $`R\epsilon`$.

## 5. Dimensionless parameters and proof route

The following conventions are used throughout:

| Symbol | Definition | Meaning |
|---|---|---|
| $`\eta`$ | $`\gamma/\Gamma`$ | Received output fraction |
| $`s`$ | $`\Omega/\Gamma`$ | Drive relative to total dephasing |
| $`r`$ | $`\Omega/(2\Gamma)=s/2`$ | Drive in the rescaled filtering equations |
| $`q`$ | $`\Omega^2/(8\Gamma\gamma)=r^2/(2\eta)`$ | Classical Wonham comparison parameter |
| $`\delta`$ | $`\Omega^2/(\Gamma\gamma)=8q`$ | Small-error parameter for the quantum converse |

There are three independent ingredients. The [counting page](counting.md) obtains an exact closed pair of correlation equations and an attainable error. The [quantum-limit page](quantum_limit.md) lower-bounds arbitrary quantum processing using a physical instrument on inaccessible output. The [homodyne page](homodyne.md) compares the exact quantum diffusion with a classical filter through a convex Poisson equation. The last step is uniform in $`q`$, which makes it strong enough to determine a logarithmic separation in [observer counts](observer_counts.md).

The classical telegraph process appears as a comparison model within that proof. The main results do not replace the driven quantum source by an assumed classical process.
