# Thirty milestones for quantum observer redundancy

A driven qubit emits one output field, which several observers receive in fixed fractions. Each observer must predict a terminal measurement of the same changing observable from its own causal record. This map develops the understanding needed to follow the receiver construction, the two lower bounds, and the resulting observer-count laws.

The selected educational anchor is **H. M. Wiseman and G. J. Milburn, *Quantum Measurement and Control*, first edition (Cambridge University Press, 2010)**, abbreviated **W&M** below. All chapter and section numbers refer to that edition. The [source bridge](source_bridge.md#selected-source) records the edition, notation and topic routes; the publisher provides a [table of contents](https://assets.cambridge.org/97805218/04424/frontmatter/9780521804424_frontmatter.pdf). The book supplies measurement and stochastic foundations. The linked scientific pages supply the project's constructions, bounds and exact assumptions.

The map contains exactly **30 milestones in two phases**. Eleven background milestones assemble three languages: quantum instruments and output fields, stochastic inference, and binary discrimination. Nineteen narrative milestones follow the local counting mechanism and the two distinct lower-bound arguments into the shared-resource result, its accuracy requirements and its interpretation. M11 and M30 synthesize their respective phases.

| Phase | Milestones | Progression |
|---|---|---|
| Background and preliminaries | M01–M11 | States and outcomes, source dynamics, output measurements, inference, then the complete causal resource task |
| Narrative and innovation | M12–M30 | Counting construction, quantum-memory converse, homodyne comparison, observer counts, imperfections, then evidence and operational meaning |

Each milestone is an understanding target with dependencies and source pointers. The two proof threads use inherited ingredients: placing Wonham filtering or binary quantum discrimination in the narrative does not make those foundations a contribution of this project. The [related-work account](../references/related-work.md) identifies their primary sources. Specialist details remain in the canonical proofs rather than being duplicated here.

## Phase I: background and preliminaries

### M01

**Qubit states and a terminal prediction**

- **Central question:** How does a quantum state determine the error of a binary prediction about a later projective test?
- **Understanding target:** Read a Bloch vector as probabilities for a specified measurement, and obtain the best sign guess and its error from the conditional Z coordinate.
- **Dependencies and story role:** Entry point. Establishes the state, observable and decision that all later receivers must connect.
- **Conceptual connection:** Born probabilities become an operational loss function only after the target measurement and the observer's information are specified.
- **Source pointers:** W&M §§1.2.1–1.2.2, quantum probability and projective measurements. Project: [Target and conditional error](../science/model.md#2-what-an-observer-must-predict).

### M02

**Measurement outcomes and conditional states**

- **Central question:** Why must a measurement specify both the probability of an outcome and the state conditioned on it?
- **Understanding target:** Distinguish a POVM effect from a quantum instrument, conditional evolution from the state obtained by forgetting the record, and an unnormalized conditional state from a normalized one.
- **Dependencies and story role:** [M01](#m01). Supplies the local measurement language needed for detector models and later information grants.
- **Conceptual connection:** Summing instrument outcomes specifies the unconditional experiment that the receiver model must reproduce.
- **Source pointers:** W&M §1.3, outcomes represented as operators, and §1.4, the most general formulation of quantum measurements. Project: [Source–bit block states](../science/counting.md#2-joint-state-of-the-source-and-stored-bit); [source-preserving output instrument](../science/quantum_limit.md#2-a-physical-instrument-on-the-inaccessible-output).

### M03

**A driven, dephasing source**

- **Central question:** What changes when a Hamiltonian rotates a qubit out of the basis selected by dephasing?
- **Understanding target:** Translate the stated Lindblad convention into Bloch equations, including off-diagonal decay at rate $`2\Gamma`$, and explain why the noncommuting drive keeps the prediction task changing.
- **Dependencies and story role:** [M01](#m01), [M02](#m02). Moves from an individual measurement to the source's continuous dynamics.
- **Conceptual connection:** A stationary unconditional state can coexist with informative, time-dependent conditional records.
- **Source pointers:** W&M §§3.2 and 3.6, Born–Markov dynamics and Lindblad positivity; §3.7, the pointer basis; §4.6, the Bloch-sphere illustration. Project: [Source convention](../science/model.md#1-source-and-output-sharing); [exact quantum Bloch diffusion](../science/homodyne.md#4-the-exact-quantum-diffusion).

### M04

**One output divided among observers**

- **Central question:** How can several output branches carry information about one source while leaving its total dynamics fixed?
- **Understanding target:** Track the distinction between total coupling $`\Gamma`$, received coupling $`\gamma`$, and inaccessible output, including the vacuum ports and fixed fractions used in passive splitting.
- **Dependencies and story role:** [M03](#m03). Adds the physical access structure on which the resource comparison depends.
- **Conceptual connection:** Disjoint output modes define separate local access; they do not imply statistically independent records of the common source.
- **Source pointers:** W&M §4.7, monitoring in the Heisenberg picture, provides the monitoring framework; the exact splitter model is specified in the project. Project: [Source and output sharing](../science/model.md#1-source-and-output-sharing); [fixed allocations](../science/observer_counts.md#1-fixed-allocations-and-the-weakest-branch).

### M05

**Counts, displacement and no-count evolution**

- **Central question:** What information is supplied by a photon count, and what information remains in the absence of a count?
- **Understanding target:** Interpret jump operators and conditional no-count evolution, and explain how a local field displacement changes the detector's outcome probabilities.
- **Dependencies and story role:** [M02](#m02), [M04](#m04). Introduces the first receiver primitive before its adaptive policy is assembled.
- **Conceptual connection:** An optical displacement can alter what a detector learns while the unconditional source generator stays fixed.
- **Source pointers:** W&M §§4.2–4.3, quantum jumps and photodetection; the particular displacement and bit policy are supplied by the project. Project: [Displaced receiver](../science/counting.md#1-the-receiver); [block and no-count generators](../science/counting.md#2-joint-state-of-the-source-and-stored-bit).

### M06

**Diffusive quadrature currents and partial detection**

- **Central question:** What distinguishes a continuously noisy quadrature current from a sequence of count events?
- **Understanding target:** Identify the homodyne current, its phase, its noise and its received fraction, and distinguish the diffusive measurement class from finite-local-oscillator photon counting.
- **Dependencies and story role:** [M04](#m04), [M05](#m05). Places the two receiver architectures on the same output model.
- **Conceptual connection:** Receiver comparisons need an explicit measurement operation; historical detector names alone do not determine the allowed class.
- **Source pointers:** W&M §4.4, homodyne detection, and §4.8, imperfect detection. Project: [Receiver classes](../science/model.md#3-receiver-classes); [diffusive observation model](../science/homodyne.md#4-the-exact-quantum-diffusion).

### M07

**Itô calculus and innovations**

- **Central question:** How does a conditional state update when the next infinitesimal current increment is observed?
- **Understanding target:** Recognize innovations as the unpredictable part of the measured current, retain Itô quadratic-variation terms, and interpret predictable control as a decision made before the next increment.
- **Dependencies and story role:** [M03](#m03), [M05](#m05), [M06](#m06). Supplies the stochastic tools shared by the filtering and moment arguments.
- **Conceptual connection:** The same infinitesimal update determines both information gained and conditional quantum backaction.
- **Source pointers:** W&M Appendix B.2, Itô calculus; Appendix B.6, general noise; §§4.4 and 4.6 for the monitored-qubit setting. Project: [Exact innovations equations](../science/homodyne.md#4-the-exact-quantum-diffusion); [integrated moment estimates](../science/homodyne.md#5-uniform-moment-estimates).

### M08

**Bayesian tracking of a changing sign**

- **Central question:** Why is estimating a sign that can change different from discriminating one fixed signal?
- **Understanding target:** Use a posterior probability as the state of an inference problem, identify its causal Bayes error, and explain the roles of transition rate and observation strength in the two-state Wonham filter.
- **Dependencies and story role:** [M01](#m01), [M07](#m07). Connects local stochastic updates to a complete classical tracking problem.
- **Conceptual connection:** The classical posterior will provide an exact comparison function for the quantum filter; it does not assign an unobserved classical path to the qubit.
- **Source pointers:** W&M §1.1.3, Bayesian inference, and §6.3, general classical systems, supply foundations; the inherited Wonham equation is developed and attributed in the project. Project: [Classical posterior dynamics](../science/homodyne.md#21-posterior-dynamics); [filtering attribution](../references/related-work.md#classical-filtering).

### M09

**Binary quantum discrimination and information ordering**

- **Central question:** How do priors and state overlap limit the accuracy of an arbitrary quantum decision?
- **Understanding target:** Interpret the minimum error for two quantum states with unequal priors, and explain why providing extra information can only improve the best decision.
- **Dependencies and story role:** [M02](#m02), [M08](#m08). Adds the quantum decision tool needed for a receiver-independent lower bound.
- **Conceptual connection:** A lower bound for a more informative discrimination experiment also limits the original receiver.
- **Source pointers:** W&M §2.7, quantum state discrimination, with §1.4 for generalized measurements. Project: [Unequal-prior discrimination bound](../science/quantum_limit.md#a-genie-that-preserves-the-zeroone-change-ambiguity); [imported ingredients](../science/quantum_limit.md#11-verification-and-imported-ingredients).

### M10

**Causality, stored output and a terminal test**

- **Central question:** What information can an observer use at the time its guess is tested?
- **Understanding target:** Separate causal records from future observations, distinguish a continuously maintained guess from one terminal collective measurement, and explain why storing all past output is a valid relaxation.
- **Dependencies and story role:** [M04](#m04), [M07](#m07), [M09](#m09). Integrates measurement and inference into an operational time ordering.
- **Conceptual connection:** Downstream processing changes an observer's knowledge without feeding back to the source; this ordering makes the final target and earlier output jointly measurable.
- **Source pointers:** W&M §§1.4 and 4.7 provide the measurement and monitoring framework. Project: [Causal guessing criterion](../science/model.md#2-what-an-observer-must-predict); [terminal-measurement relaxation](../science/quantum_limit.md#9-why-the-bound-applies-to-continuous-operation).

### M11

**The complete resource and error task**

- **Central question:** What must be fixed before two observer-count claims can be compared?
- **Understanding target:** State the source, allowed local operations, fixed output allocation, long-run marginal error and supplied apparatus resources together, including the order of limits and the absence of communication or source feedback.
- **Dependencies and story role:** [M06](#m06), [M08](#m08), [M09](#m09), [M10](#m10). Synthesizes the background into the complete problem used by every subsequent theorem.
- **Conceptual connection:** The charged resource is total source coupling; a claim about each observer's accuracy has different content from a claim about simultaneous unanimous agreement.
- **Source pointers:** W&M §§1.4, 2.7, 4.7 and 4.8 supply the measurement, decision and access language; the resource task is defined by the project. Project: [Model and definitions](../science/model.md); [resource and observer count](../science/model.md#4-the-resource-and-the-observer-count).

## Phase II: narrative and innovation

The counting and quantum-limit thread runs from M12 to M19. The classical-reference and exact-quantum homodyne thread runs from M20 to M23. They meet at M24 and support the allocation, capacity and interpretation milestones that follow.

### M12

**The one-bit nulling mechanism**

- **Central question:** How can one stored bit determine a receiver setting that corrects the guess when a photon is counted?
- **Understanding target:** Explain why the displacement makes the currently guessed pointer sign dark, why a count selects the opposite sign, and why flipping the bit then makes it agree with that conditional state.
- **Dependencies and story role:** [M05](#m05), [M11](#m11). Starts the narrative with a concrete local receiver whose performance can be calculated.
- **Conceptual connection:** Established nulling and adaptive finite-state ideas become a specific partial-output prediction policy; the controller bit stores a guess, not the full conditional quantum state.
- **Source pointers:** W&M §§4.2–4.3 provide jump and photodetection foundations. Project: [Receiver action](../science/counting.md#1-the-receiver); [prior nulling and finite-state monitoring](../references/related-work.md#nulling-and-finite-state-tracking).

### M13

**Exact error from two correlations**

- **Central question:** Why does the performance of this quantum receiver reduce to two linear equations?
- **Understanding target:** Follow the source–bit block generator, identify the correlations that close, and distinguish the exact finite-drive stationary error from its small-error leading term.
- **Dependencies and story role:** [M03](#m03), [M07](#m07), [M12](#m12). Converts the mechanism into an attainable quantitative bound.
- **Conceptual connection:** A finite controller can have an exactly calculable prediction error even when the underlying conditional source state is not restricted to two pure states.
- **Source pointers:** W&M §3.6 and §4.6 provide master-equation and Bloch-coordinate foundations; the correlation closure is proved in the project. Project: [Joint block dynamics](../science/counting.md#2-joint-state-of-the-source-and-stored-bit); [exact closure and error](../science/counting.md#3-exact-correlation-closure).

### M14

**A physical measurement of the lost output**

- **Central question:** What extra information can a lower-bound proof provide without changing the original observed experiment?
- **Understanding target:** Explain how splitting, real displacement and counting of inaccessible output produce rank-one Z jumps at a state-independent Poisson rate while preserving the unconditional source dynamics.
- **Dependencies and story role:** [M02](#m02), [M04](#m04), [M05](#m05), [M11](#m11). Begins the unrestricted converse with a physically valid local instrument.
- **Conceptual connection:** Measuring an already inaccessible output preserves the original marginal experiment; an arbitrary inserted source measurement need not do so.
- **Source pointers:** W&M §§1.4 and 4.2–4.3 provide instrument and counting foundations; this lost-output construction is explicit in the project. Project: [Physical lost-output instrument](../science/quantum_limit.md#2-a-physical-instrument-on-the-inaccessible-output).

### M15

**A revealed event removes dependence on older memory**

- **Central question:** Why can a known rank-one event make arbitrary older quantum memory irrelevant to the subsequent discrimination problem?
- **Understanding target:** Use the conditional tensor-product identity after a rank-one projection, together with independent future vacuum inputs, to identify exactly which past correlations are removed.
- **Dependencies and story role:** [M10](#m10), [M14](#m14). Turns the physical instrument into the step that handles unlimited receiver memory.
- **Conceptual connection:** The argument removes dependence on old memory by a genuine conditional event; it does not assume that the observer had already measured its stored field.
- **Source pointers:** W&M §§1.4 and 4.7 supply conditioning and monitoring foundations; the memory argument is proved locally. Project: [Memory factorization](../science/quantum_limit.md#3-a-genuine-event-screens-arbitrary-older-quantum-memory).

### M16

**Pure fields on intervals between events**

- **Central question:** What quantum states must be compared after the source has been reset to a known sign?
- **Understanding target:** Interpret the source–field isometry on one interval, the endpoint transition probability and the two field overlaps, and explain why conditioned interval fields form tensor products.
- **Dependencies and story role:** [M03](#m03), [M09](#m09), [M15](#m15). Reduces an arbitrary history to finite discrimination data.
- **Conceptual connection:** Known pointer endpoints create an exact conditional decomposition, while coherent source evolution within each interval remains fully quantum.
- **Source pointers:** W&M §§1.4, 3.2 and 4.7 provide channel and monitoring foundations. Project: [Interval field states and overlaps](../science/quantum_limit.md#4-pure-interval-fields-and-a-finite-discrimination-experiment); [reduced-channel formulas](../science/quantum_limit.md#5-local-interval-estimates).

### M17

**A genie that retains the difficult ambiguity**

- **Central question:** How can extra classical information simplify the interval experiment without revealing the answer in every case?
- **Understanding target:** Explain the randomized index supplied on zero-change and one-change branches, retain its unequal unnormalized priors, and connect the resulting pure-state overlap to the inherited Helstrom bound.
- **Dependencies and story role:** [M08](#m08), [M09](#m09), [M16](#m16). Builds the finite discrimination inequality used by the converse.
- **Conceptual connection:** A useful information grant preserves a controlled binary ambiguity; replacing its priors by equal priors would change the experiment.
- **Source pointers:** W&M §1.1.3 for Bayesian weights and §2.7 for quantum discrimination; the randomized genie is constructed in the project. Project: [Genie messages and priors](../science/quantum_limit.md#a-genie-that-preserves-the-zeroone-change-ambiguity); [finite-partition relaxation](../science/quantum_limit.md#a-useful-relaxation).

### M18

**Local remainder control and the renewal coefficient**

- **Central question:** How can a perturbative calculation remain valid when the total observation window is long?
- **Understanding target:** Distinguish expansions on individual lost-event intervals from an expansion over the whole window, and explain how Poisson averaging controls the remainder and fixes the leading coefficient.
- **Dependencies and story role:** [M07](#m07), [M16](#m16), [M17](#m17). Assembles the interval bounds into a uniform quantitative estimate.
- **Conceptual connection:** The truncated final interval contributes to the renewal coefficient; rare long intervals are controlled in the moment bound rather than removed by a cutoff.
- **Source pointers:** W&M §4.2 and Appendix B.6 provide jump-process foundations; the interval estimates and renewal calculation are project proofs. Project: [Local estimates](../science/quantum_limit.md#5-local-interval-estimates); [Poisson remainder](../science/quantum_limit.md#6-poisson-averaging-of-the-remainder); [renewal coefficient](../science/quantum_limit.md#7-the-exact-renewal-coefficient).

### M19

**The unrestricted partial-output quantum limit**

- **Central question:** How do the reset window and discrimination bound limit every causal quantum receiver?
- **Understanding target:** Connect the first genuine event in the window to the uniform lower bound for received fractions at most one half, match its leading coefficient to counting, and identify why complete collection is a separate case.
- **Dependencies and story role:** [M13](#m13), [M15](#m15), [M17](#m17), [M18](#m18). Completes the first lower-bound thread.
- **Conceptual connection:** The converse grants stronger terminal quantum processing than continuous reporting requires, yet partial output loss still imposes a positive leading prediction error.
- **Source pointers:** W&M §§2.7 and 4.7 supply discrimination and causal-monitoring foundations; the quantitative theorem and full-output exception are proved in the project. Project: [Window argument](../science/quantum_limit.md#8-inserting-the-bound-into-an-arbitrary-past-history); [continuous operation](../science/quantum_limit.md#9-why-the-bound-applies-to-continuous-operation); [complete-output exception](../science/quantum_limit.md#10-complete-output-access-is-a-genuine-exception).

### M20

**The inherited classical tracking law**

- **Central question:** Where does the logarithm in the classical causal tracking error enter?
- **Understanding target:** Follow the Wonham posterior's invariant density, its exact Bessel-function error and the small-$`q`$ expansion, while distinguishing this classical reference from the exact quantum source.
- **Dependencies and story role:** [M08](#m08), [M11](#m11). Opens the second lower-bound thread with its established classical ingredient.
- **Conceptual connection:** A stationary distribution of posterior confidence determines the optimal classical decision error; obtaining a quantum statement still requires a controlled comparison.
- **Source pointers:** W&M §1.1.3, §6.3 and Appendix B.5 provide Bayesian and diffusion foundations. The Wonham filter is inherited; the explicit reference calculation and primary attribution are supplied in the project. Project: [Exact classical error](../science/homodyne.md#2-the-classical-wonham-error); [classical-filtering references](../references/related-work.md#classical-filtering).

### M21

**A convex Poisson solution**

- **Central question:** What comparison function can keep an approximation error small relative to the tracking error itself?
- **Understanding target:** Explain the Poisson equation for the binary loss, why its solution is convex, why its gradient has size $`e_{\mathrm W}(q)`$, and why its endpoint regularity permits ordinary Itô calculus.
- **Dependencies and story role:** [M07](#m07), [M08](#m08), [M20](#m20). Supplies the analytical tool that makes the quantum comparison relative rather than merely absolute.
- **Conceptual connection:** Concavity of an optimal Bayes risk in the prior leads to convexity of the integrated comparison function; endpoint derivatives fix the sharp gradient scale.
- **Source pointers:** W&M §1.1.3 and Appendices B.2 and B.5 provide Bayesian and stochastic-calculus foundations. The particular Poisson solution, convexity and endpoint proof are supplied by the project. Project: [Convex Poisson lemma](../science/homodyne.md#3-a-convex-poisson-solution-with-a-sharp-gradient-bound).

### M22

**The exact source compared with the classical filter**

- **Central question:** Which part of the exact quantum filter remains after the fast transverse coordinate is eliminated only in a controlled estimate?
- **Understanding target:** Translate the source filter into scaled coordinates, identify the deviation variable, and connect its moment bound to the two-sided relative error estimate for the real quadrature.
- **Dependencies and story role:** [M03](#m03), [M06](#m06), [M07](#m07), [M21](#m21). Transfers the classical reference into an exact-source theorem.
- **Conceptual connection:** The comparison bounds a correction inside the full quantum equations; it does not require trace-norm convergence of the output to a classical telegraph field.
- **Source pointers:** W&M §§4.4, 4.6 and 4.8 and Appendix B.2 supply the quantum-filter and Itô foundations. Project: [Exact quantum diffusion](../science/homodyne.md#4-the-exact-quantum-diffusion); [real-quadrature moment estimate](../science/homodyne.md#51-real-quadrature); [error comparison](../science/homodyne.md#6-comparing-the-exact-error-with-the-wonham-error).

### M23

**Every predictable quadrature phase**

- **Central question:** Can a phase chosen from the entire past record remove the leading homodyne tracking penalty?
- **Understanding target:** Identify the phase-dependent terms in the exact filter, explain the nonnegative Poisson contribution and uniform moment control, and state the long-run lower bound without assuming a stationary controller.
- **Dependencies and story role:** [M10](#m10), [M21](#m21), [M22](#m22). Completes the second lower-bound thread over the full defined homodyne class.
- **Conceptual connection:** An arbitrary classical feedback policy for the detector phase is allowed; finite-local-oscillator counting and general field preprocessing remain different measurement operations.
- **Source pointers:** W&M §4.4 and Appendix B.2 provide diffusive-measurement and stochastic-calculus foundations; the all-policy bound is proved in the project. Project: [Adaptive-phase moments](../science/homodyne.md#52-arbitrary-predictable-phase); [long-run comparison](../science/homodyne.md#6-comparing-the-exact-error-with-the-wonham-error); [uniform regime](../science/homodyne.md#7-uniform-asymptotic-regime).

### M24

**The matched single-observer frontiers**

- **Central question:** What is established when the construction and both lower bounds are placed in the same parameter regime?
- **Understanding target:** Distinguish exact counting performance, asymptotic unrestricted optimality and the relative homodyne bracket, and explain their different leading errors at small received fraction and small $`q`$.
- **Dependencies and story role:** [M13](#m13), [M19](#m19), [M20](#m20), [M23](#m23). Joins the two proof threads before output is allocated among many observers.
- **Conceptual connection:** Receiver architecture changes the accessible prediction accuracy even though the source and its total dephasing are unchanged.
- **Source pointers:** W&M §2.7 and §§4.2–4.4 provide the discrimination and measurement foundations; the matched frontier is assembled from the project theorems. Project: [Finite-parameter ingredients](../science/observer_counts.md#2-finite-parameter-ingredients); [quantum theorem](../science/quantum_limit.md#1-model-receiver-class-and-result); [homodyne theorem](../science/homodyne.md#1-measurement-class-and-result).

### M25

**Why equal sharing is optimal**

- **Central question:** Could an unequal fixed allocation support more marginally accurate observers?
- **Understanding target:** Use the weakest branch, emulate its actual receiver with stronger access, and explain classical current degradation within the diffusive homodyne class without assuming an optimizer is attained.
- **Dependencies and story role:** [M04](#m04), [M09](#m09), [M11](#m11), [M24](#m24). Converts single-observer performance into a statement about all fixed allocations.
- **Conceptual connection:** Access monotonicity and a marginal error criterion let independent copies of an actual receiver establish equal-sharing feasibility despite correlated source records.
- **Source pointers:** W&M §1.4 and §4.8 provide generalized-measurement and partial-detection foundations; the allocation argument is supplied by the project. Project: [Weakest-branch proof](../science/observer_counts.md#1-fixed-allocations-and-the-weakest-branch); [measurement classes](../science/model.md#3-receiver-classes).

### M26

**From error to the observer-count laws**

- **Central question:** How do the two single-observer errors determine optimal integer observer counts?
- **Understanding target:** Follow the attainable and excluded threshold counts, retain the joint accuracy/drive condition, and explain why monotonicity excludes larger counts without extrapolating a small-parameter remainder.
- **Dependencies and story role:** [M24](#m24), [M25](#m25). Establishes the project's shared-resource consequence.
- **Conceptual connection:** The homodyne logarithm becomes a logarithmic ratio of observer capacities only in a regime where both counts diverge and integer rounding becomes negligible.
- **Source pointers:** W&M §2.7 supplies the decision-error foundation; the resource inversion and joint limit are project results. Project: [Observer-count theorem and threshold proofs](../science/observer_counts.md#3-the-observer-count-theorem).

### M27

**An imperfect counting instrument**

- **Central question:** How do displacement mismatch and false clicks alter the exact source–guess dynamics?
- **Understanding target:** Retain the complex-displacement instrument correction, distinguish it from physical source feedback, and obtain the meaning of the exact stationary accuracy condition for the specified click-and-flip policy.
- **Dependencies and story role:** [M02](#m02), [M05](#m05), [M13](#m13). Extends the constructive result while keeping its source model and policy explicit.
- **Conceptual connection:** An apparent Hamiltonian term in a detector representation can be required to preserve the original source generator rather than describe an applied control field.
- **Source pointers:** W&M §§1.4, 4.3 and 4.8 provide instrument and imperfect-detection foundations; the complex-calibration and dark-click formulas are supplied by the project. Project: [Imperfect instrument](../science/imperfections.md#1-a-source-preserving-imperfect-instrument); [exact stationary error](../science/imperfections.md#2-exact-stationary-error).

### M28

**What detector accuracy the ideal count requires**

- **Central question:** When does detector noise change the leading coefficient or prevent a stringent target from being reached?
- **Understanding target:** Separate calibration and dark-count floors from loss of received signal, and relate their required scaling to the many-observer accuracy budget.
- **Dependencies and story role:** [M26](#m26), [M27](#m27). Connects the ideal capacity theorem to the conditions under which its explicit receiver retains that performance.
- **Conceptual connection:** Fixed noise does not disappear when the drive is weakened; the exact inequality determines which part of the error budget remains available for tracking.
- **Source pointers:** W&M §4.8 provides the imperfect-detection foundation; the project gives the finite accuracy inequality and its asymptotic scaling. Project: [Accuracy budget](../science/imperfections.md#3-what-consumes-the-accuracy-budget); [detection loss and sharing](../science/imperfections.md#4-inefficient-detection-and-output-sharing).

### M29

**Analytical proof, numerical evidence and attribution**

- **Central question:** What supports each part of the result, and which conclusions cannot be established by finite numerical checks?
- **Understanding target:** Match augmented-generator, Choi, overlap, quadrature and renewal checks to the algebra they test; distinguish those checks from the physical genie and arbitrary-policy proofs; identify the inherited filtering, discrimination and receiver ideas.
- **Dependencies and story role:** [M18](#m18), [M21](#m21), [M23](#m23), [M28](#m28). Reviews the assembled result through its evidence and source dependencies.
- **Conceptual connection:** Independent finite constructions can detect convention or coefficient errors, while uniform guarantees and the scope of a contribution require their analytical and bibliographic arguments.
- **Source pointers:** W&M §3.6 and Appendix B.5 provide positivity and diffusion foundations. The project verification route and primary related-work account supply the evidence and attribution boundaries. Project: [Verification coverage](../verification/README.md#what-is-checked); [analytical obligations](../verification/README.md#what-remains-analytical); [related work and contribution](../references/related-work.md).

### M30

**The operational meaning of quantum observer redundancy**

- **Central question:** What can the complete argument say about many observers agreeing on a changing quantum observable?
- **Understanding target:** Explain the optimal quantum count, the smaller diffusive-homodyne count and their logarithmic ratio together with fixed sharing, causal access, apparatus assumptions, calibration requirements and the distinction between marginal accuracy and unanimity.
- **Dependencies and story role:** [M11](#m11), [M19](#m19), [M24](#m24), [M26](#m26), [M28](#m28), [M29](#m29). Synthesizes the narrative from local receiver actions to the full operational contribution and its limits.
- **Conceptual connection:** The conclusion concerns how a specified quantum output supports accurate current guesses. It neither assigns a classical trajectory to the source nor establishes simultaneous independent observer errors.
- **Source pointers:** W&M §§1.4, 2.7, 4.7 and 4.8 provide the common measurement, decision, monitoring and access framework; the combined scientific statement resides in the project. Project: [Physical interpretation](../science/observer_counts.md#5-physical-interpretation); [marginal resource criterion](../science/model.md#4-the-resource-and-the-observer-count); [scientific proof route](../science/README.md).
