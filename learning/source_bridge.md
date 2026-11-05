# From quantum measurement theory to observer redundancy

A continuously monitored qubit produces a field that several observers can share. The observers agree on the source dynamics, but each receives only a fraction of the output and must decide what measurement to perform on it. This project asks how that choice affects the number of observers who can predict a present measurement outcome accurately.

Wiseman and Milburn's book supplies the measurement and trajectory framework for approaching this question. The project then supplies two different optimality arguments: a quantum discrimination argument that permits coherent receiver memory, and a stochastic comparison argument for diffusive homodyne measurements. This bridge explains the transitions between those levels. The complete statements and proofs remain in the linked scientific pages.

## Selected source

**Howard M. Wiseman and Gerard J. Milburn, *Quantum Measurement and Control*, first edition, Cambridge University Press, 2010.** ISBN 9780521804424; DOI [10.1017/CBO9780511813948](https://doi.org/10.1017/CBO9780511813948).

The [publisher's frontmatter and contents](https://assets.cambridge.org/97805218/04424/frontmatter/9780521804424_frontmatter.pdf) confirm the edition's publication year and the section references below. The [publisher's opening excerpt](https://assets.cambridge.org/97805218/04424/excerpt/9780521804424_excerpt.pdf) provides pages 1–10, including Bayesian conditioning and the introduction to projective measurement.

| Source sections | Use in this project |
|---|---|
| §§1.1–1.4 | Probabilities, conditional states, measurement outcomes, and general measurement operations |
| §2.7 | Binary quantum discrimination |
| §§3.2, 3.6–3.8 | Markov evolution, Lindblad generators, pointer states, and conditional ensembles |
| §§4.2–4.4 | Counting and diffusive optical observations |
| §§4.6–4.8 | Qubit trajectories, output monitoring, and imperfect detection |
| Appendix B, especially B.2, B.5–B.6 | Itô calculus, stationary diffusion equations, and counting noise |

These sections are entry points into the relevant foundations. The exact source, receiver policies, converse, and uniform asymptotic comparisons are derived in this repository. The primary research literature remains separately attributed in [related work](../references/related-work.md); it is not an additional educational anchor.

## Project conventions

The book's opening excerpt uses $`X,Y`$ for classical system and readout random variables and calls $`\rho`$ a state matrix. Here $`X,Y,Z`$ are **Pauli operators**, while $`\rho`$ is also called a density operator. A subscripted $`Y_t`$ in a homodyne equation is an integrated classical detector current, not the Pauli operator $`Y`$. The distinction is the role of the object, not the letter alone.

All equations and rate conventions below are those of the project. In units with $`\hbar=1`$,

```math
H=\frac{\Omega X}{2},
\qquad
\mathcal L\rho=-i[H,\rho]+\Gamma\mathcal D[Z]\rho,
\qquad
\mathcal D[L]\rho=L\rho L^\dagger-\frac12\{L^\dagger L,\rho\}.
```

This normalization makes a source coherence decay at rate $`2\Gamma`$ in the absence of the drive. It makes an incorrectly nulled pointer state produce counts at rate $`4\gamma`$ in a branch of strength $`\gamma`$. Both factors enter the final error coefficients, so replacing $`\Gamma`$ by an informally named “dephasing rate” can introduce a factor of two.

| Project object | Meaning and distinction |
|---|---|
| $`\rho_t=(I+x_tX+y_tY+z_tZ)/2`$ | Normalized source state conditioned on a particular observer's classical record |
| $`\rho_g`$, $`g=\pm1`$ | Unnormalized source block for a stored guess; its trace is the probability of that controller sector |
| $`\Gamma`$ and $`\gamma`$ | Total dephasing strength and one observer's received share, respectively |
| $`\eta=\gamma/\Gamma`$ | Received fraction; it is not a detector quantum efficiency unless a physical loss model makes that identification |
| $`r=\Omega/(2\Gamma)`$, $`q=\Omega^2/(8\Gamma\gamma)`$, $`\delta=8q`$ | Dimensionless drive and error-comparison parameters; none is an observed error probability by definition |
| $`e_{\mathrm{null}}`$, $`e_{\mathrm Q}`$, $`e_{\mathrm H}`$ | Error of a specified receiver, optimum quantum error, and optimum diffusive homodyne error, respectively |

The resource assumptions also need translation into a concrete experiment. Vacuum input fields interact with one fixed source. A passive splitter assigns constant output fractions, with $`\sum_i\gamma_i\le\Gamma`$. Phase references and local receiver controls are supplied. The budget is the total source coupling, not local-oscillator energy, detector bandwidth, or memory size.

Adaptation acts on the **outgoing field**: a receiver changes its displacement or quadrature phase using its own earlier record. It never changes the source Hamiltonian or feeds a field back into the source. Separate observers do not exchange records. These restrictions are part of the [model](../science/model.md), rather than generic assumptions of quantum control theory.

## Prediction and output measurements

The first transition from measurement theory to this project is a choice of loss function. An observer is not asked to reconstruct the entire state or estimate an unknown Hamiltonian parameter. It must guess the result of one terminal projective $`Z`$ measurement.

For a classical record with conditional coordinate $`z`$, the two outcome probabilities are $`(1+z)/2`$ and $`(1-z)/2`$. Choosing the more probable sign therefore gives

```math
h(z)=\frac{1-|z|}{2}.
```

For example, the pure state $`(I+0.6X+0.8Z)/2`$ assigns probability $`0.9`$ to the positive outcome. The best bit is positive and its error is $`0.1`$. Purity alone does not determine this error; the orientation relative to the tested observable matters.

The conditional state summarizes knowledge after a specified classical measurement of the output. An observer retaining quantum field modes has a larger decision problem. Its stored field need not be replaceable by a classical posterior coordinate without losing useful information. This is why an optimal classical filter does not by itself prove an unrestricted quantum receiver bound.

The earlier output and the terminal source observable are compatible measurements. The experiment can run until a fixed terminal time, or an independently sampled test time, then read the receivers and perform the source test. Long-run mean error averages the errors of such stopped experiments. It does not repeatedly project the source during its evolution. See [the prediction criterion](../science/model.md#2-what-an-observer-must-predict).

## The one-bit counting receiver

The counting foundations in §§4.2–4.3 become a concrete receiver after a policy is specified. Store a guess $`g\in\{-1,+1\}`$ and displace the received field by $`-g\sqrt\gamma`$. The resulting jump operator is

```math
J_g=\sqrt\gamma(Z-gI).
```

Take $`g=+1`$. A positive pointer state is dark because $`J_+|+\rangle=0`$; a negative pointer state has count intensity $`4\gamma`$. A registered click projects the conditional source state onto the negative pointer state. Flipping the stored bit then makes that state dark. The same reasoning applies with the signs reversed.

Between clicks, the Hamiltonian and the no-count evolution remain active. Describing only a sequence of hypothetical classical sign changes would omit that quantum evolution. The project instead evolves the two unnormalized blocks $`\rho_+,\rho_-`$. Their sum obeys the original source master equation, which checks that the adaptive output measurement has not introduced source feedback.

The project-provided simplification is that two correlations close:

```math
c_z=\sum_g g\mathrm{Tr}(Z\rho_g),
\qquad
c_y=\sum_g g\mathrm{Tr}(Y\rho_g),
```

```math
\dot c_z=\Omega c_y+4\gamma(1-c_z),
\qquad
\dot c_y=-\Omega c_z-2\Gamma c_y.
```

The guessing error is $`(1-c_z)/2`$. Solving the stable two-dimensional system gives

```math
e_{\mathrm{null}}
=\frac{\Omega^2}{2(\Omega^2+8\Gamma\gamma)}
=\frac{\delta}{16+2\delta}.
```

This is an exact stationary performance calculation for the specified receiver. It is not an exact finite-parameter optimum over all receivers. [The counting proof](../science/counting.md) derives the block equation, closure, and convergence. The established nulling and adaptive finite-state precedents are credited in [the receiver comparison](../references/related-work.md#nulling-and-finite-state-tracking).

## The partial-output quantum converse

The next transition uses the discrimination framework associated with §2.7, together with the distinction between unconditional evolution and a conditional trajectory. The task is now to show that even a receiver with all its past output stored coherently cannot improve the leading counting coefficient.

A lower bound becomes easier if extra information is granted to the observer. Such a grant must preserve the observed-output experiment. Inserting an arbitrary projective measurement directly on the source would generally change its correlations with the old field and would not be a valid shortcut.

The project supplies an actual instrument on the **inaccessible** output. Let $`\kappa=\Gamma-\gamma`$. Splitting that output, applying opposite displacements, and counting produces jump operators

```math
L_+=\sqrt{2\kappa}\,P_+,
\qquad
L_-=-\sqrt{2\kappa}\,P_-,
\qquad
P_\pm=\frac{I\pm Z}{2}.
```

Their total intensity is $`2\kappa I`$. Thus the event times form a Poisson process with state-independent rate $`2\kappa`$. Forgetting this extra record preserves the full source–received-field marginal. Revealing selected parts of the record gives the observer extra information while keeping the original prediction problem intact.

A genuine event with revealed sign $`s`$ screens all older memory $`M`$ through

```math
(P_s\otimes I_M)\rho_{SM}(P_s\otimes I_M)
=P_s\otimes\langle s|\rho_{SM}|s\rangle.
```

After conditioning on that event, the source is a known pointer state and is uncorrelated with the older memory. Fresh vacuum inputs are independent of both. This is the step that makes the argument apply to quantum memory, rather than just classical detector records.

The remaining argument has three research-level components. First, exact source–field evolution determines overlaps of the pure field states between successive events. Second, carefully chosen additional messages reduce part of the task to binary discrimination without inadvertently revealing the answer. Third, a renewal average sums the interval contributions, including the final incomplete interval. The standard Helstrom bound is the imported discrimination ingredient; these reductions and quantitative estimates are supplied by [the quantum-limit proof](../science/quantum_limit.md).

The result matches counting to leading order as $`\delta\to0`$, uniformly for $`0<\gamma/\Gamma\le1/2`$. The textbook's trajectory language is preparation for this proof, not a proof of its memory-screening or renewal estimates. The complete-output endpoint $`\gamma=\Gamma`$ is different: there is no lost field to supply these events, and coherent collection of the whole output can do better. That [endpoint exception](../science/quantum_limit.md#10-complete-output-access-is-a-genuine-exception) is part of the result's scope.

## The diffusive homodyne comparison

The homodyne and stochastic-calculus sections prepare a different route. A receiver measures a quadrature current and can choose its phase using everything in its own past classical record. With the project's normalization,

```math
dY_t=2\sqrt\gamma\cos\theta_t\,z_t\,dt+dW_t,
```

where $`W_t`$ is the innovation Brownian motion. The conditional state has both information gain and phase-dependent stochastic backaction. A phase choice therefore cannot be evaluated solely by the current's mean signal.

The class here is **diffusive homodyne with arbitrary predictable phase**. Predictability means choosing the next phase before the corresponding new noise increment is known. The historical use of “adaptive homodyne” for finite-local-oscillator photon counting does not enlarge this diffusion model. General Gaussian preprocessing and retained quantum field modes are separate receiver operations; see [the class definition](../science/homodyne.md#1-measurement-class-and-result).

### A classical comparison needs quantitative control

The binary Wonham filter supplies a classical reference. Its stationary Bayes error satisfies

```math
e_{\mathrm W}(q)\sim\frac q4\log\frac1q
\qquad(q\to0).
```

The filtering equation is an established ingredient. The repository derives the invariant density and exact Bessel expression used here and attributes the underlying filtering and special-function results in [classical filtering](../references/related-work.md#classical-filtering). This specific calculation is not assigned to an unverified textbook subsection.

It is insufficient to say that the driven qubit approaches a classical telegraph process. An approximation error that tends to zero could still be larger than the small tracking error being estimated. The comparison must be **relative to** $`e_{\mathrm W}(q)`$.

### Why the Poisson solution changes the argument

The project constructs a function $`f_q`$ solving a Poisson equation for the classical posterior generator $`\mathcal A_q`$:

```math
\mathcal A_q f_q=h-e_{\mathrm W}(q),
\qquad
f_q''\ge0,
\qquad
\|f_q'\|_\infty=e_{\mathrm W}(q).
```

The equation turns a time-averaged error into terms that can be estimated using the exact quantum dynamics. The gradient identity makes the troublesome correction proportional to the error scale itself. Convexity makes the contribution from reducing the measured signal quadrature nonnegative in the lower-bound identity. These are the reasons that arbitrary adaptive phase cannot remove the leading logarithm.

Moment estimates for the remaining qubit coordinates then give the finite-parameter bracket

```math
e_{\mathrm W}(q)[1-T_{\mathrm{ad}}(r,\eta)]
\le e_{\mathrm H}
\le e_{\mathrm W}(q)[1+T(r,\eta)],
\qquad r^2+\eta<1.
```

The [homodyne theorem](../science/homodyne.md) defines the explicit correction functions and proves that they are $`O(r^2+\sqrt\eta)`$ uniformly in $`q`$. The lower bound holds for every permitted phase policy; the fixed real quadrature supplies the upper bound. It does not say that every policy performs equally well.

Taking $`\eta\to0`$ and $`q\to0`$ therefore determines the **optimum** homodyne error. Long-run averaging is performed at each fixed parameter triple before that limit. The convex Poisson solution, its endpoint regularity, the moment bounds, and the adaptive-phase comparison are project-provided derivations; Appendix B supplies their stochastic-calculus language.

## From error to observer count

A single-receiver result becomes a resource statement only after specifying how receivers share the output. With equal fractions, $`\gamma=\Gamma/R`$. With unequal fixed fractions, at least one observer receives no more than this. A stronger branch can emulate a weaker one by discarding information. Thus an actual successful weakest-branch receiver can be copied to every equally supplied observer. This establishes equal-allocation optimality for the marginal criterion without assuming that an abstract error infimum is attained.

The exact counting formula can be inverted directly. Inverting the homodyne law requires tracking the logarithm and the simultaneous parameter limit. Write $`s=\Omega/\Gamma`$. The project proves

```math
R_{\mathrm Q}\sim\frac{16\epsilon}{s^2},
\qquad
R_{\mathrm H}\sim\frac{32\epsilon}{s^2\log(1/\epsilon)},
```

provided $`\epsilon\to0`$, $`s\to0`$, and $`s^2\log(1/\epsilon)=o(\epsilon)`$. The last condition makes both counts diverge, so integer rounding and weak-fragment limits are controlled. It is not legitimate to infer an unbounded ratio merely by sending the tolerance to zero at a fixed nonzero drive ratio.

[The count proof](../science/observer_counts.md) sandwiches attainable and excluded observer numbers. This inversion and allocation argument are supplied by the project. The criterion constrains each observer's individual error. It gives pairwise disagreement bounds, but it does not assert simultaneous unanimity of arbitrarily many observers.

## Calibration, loss, and dark counts

The imperfect-detection route in §4.8 motivates asking what is lost when an output is not fully detected. Here a detector efficiency $`\xi`$ is modeled by reducing the received strength to $`\gamma=\xi\gamma_{\mathrm{raw}}`$ while leaving the source's total $`\Gamma`$ unchanged.

The project also analyzes a specific imperfect counting policy. Replace the ideal displacement by $`\beta=a e^{i\phi}`$ relative to the intended amplitude, and let independent dark clicks of rate $`d`$ flip the bit. The actual jump becomes $`\sqrt\gamma(Z-g\beta I)`$. A complex displacement introduces a Hamiltonian term in the equivalent no-count representation. It must cancel the corresponding dissipator term so that forgetting the record still gives the original source generator. This representation term is not permission to feed a drive back to the source.

[The imperfection calculation](../science/imperfections.md) provides an exact error and tolerance inequality. Near the ideal regime, it separates the leading contributions as

```math
e_\beta
=\frac{|1-\beta|^2}{4}
+\frac d{4\gamma}
+\frac{\delta}{16}
+o\!\left(|1-\beta|^2+\frac d\gamma+\delta\right).
```

Thus retaining the ideal leading coefficient requires $`|1-\beta|^2=o(\delta)`$ and $`d=o(\Omega^2/\Gamma)`$. The result explains an accuracy budget for the specified flip-after-click receiver. It does not prove that its noisy error floor is unavoidable for every possible receiver. Finite response time and temporally correlated calibration noise require a different detector model.

## Reading the complete argument

The conceptual route joins three kinds of material:

| Foundation | Additional project step | Authoritative destination |
|---|---|---|
| Conditional measurement and open-system dynamics | Define a causal terminal-outcome loss and a fixed output budget | [Model](../science/model.md) |
| Counting instruments and adaptive measurement | Close the source–guess correlations and obtain an exact attainable error | [Counting](../science/counting.md) |
| Binary quantum discrimination and conditional trajectories | Preserve the actual output experiment, screen old memory, and average exact interval overlaps | [Quantum converse](../science/quantum_limit.md) |
| Diffusive monitoring and stochastic calculus | Construct a convex Poisson solution and a uniform relative comparison | [Homodyne theorem](../science/homodyne.md) |
| An error criterion and fixed resource allocation | Invert matched error laws in a controlled joint limit | [Observer counts](../science/observer_counts.md) |
| Imperfect output detection | Derive a source-preserving noisy instrument and its accuracy budget | [Imperfections](../science/imperfections.md) |

The [30-milestone map](milestones.md) organizes the understanding targets across this material. The [scientific entrypoint](../science/README.md) connects the proofs, and [verification](../verification/README.md) explains what the finite numerical checks establish. The textbook supplies a coherent way into the measurement theory; the repository supplies the specialized argument and its limitations.
