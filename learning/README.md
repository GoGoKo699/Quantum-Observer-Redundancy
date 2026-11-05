# Learning route

The project asks how many observers can track one changing qubit when they share a fixed output field. Understanding the answer requires three connected ideas: what an output measurement does, how a causal record supports a prediction, and how a discrimination bound constrains every receiver.

The single educational anchor is **Howard M. Wiseman and Gerard J. Milburn, *Quantum Measurement and Control*, first edition (Cambridge University Press, 2010)**, [DOI: 10.1017/CBO9780511813948](https://doi.org/10.1017/CBO9780511813948). The [source bridge](source_bridge.md#selected-source) gives verified publisher material, relevant sections and the project's notation. Reading the entire book is not a prerequisite for following the route.

## Choose a route through the same scientific account

| Purpose | Route |
|---|---|
| See the physical operation and its consequences | Start with the [worked tutorial](tutorial.md), then follow its links to the proofs. |
| Organize the complete conceptual story | Use the [30-milestone map](milestones.md). Each target records its question, dependencies, conceptual connection and sources. |
| Connect the book to this project | Read the [source bridge](source_bridge.md) alongside the relevant book sections and canonical scientific pages. |
| Inspect the theorems directly | Use the [science entrypoint](../science/README.md), then the [verification account](../verification/README.md). |

The map has **11 background milestones and 19 narrative milestones**. The background connects individual states, instruments and stochastic updates to the complete resource task. The narrative connects the counting receiver and two different lower-bound arguments to observer counts, detector accuracy and operational meaning. M11 and M30 integrate their respective phases.

The tutorial supplies worked examples and the main logical connections. The bridge identifies what the selected source prepares and what the project must derive. The map is an understanding guide, not a claim to cover every technical lemma. Exact hypotheses and proofs remain in `science/`; inherited ingredients and their primary references remain in the [related-work account](../references/related-work.md).

## The distinctions to keep throughout

The target is a terminal projective Z outcome at a fixed or independently sampled test time. Accuracy is each observer's long-run marginal error. The total source coupling and output fractions are fixed, and no observer sends feedback to the source or communicates with another observer.

The counting receiver has an exact finite-parameter error formula. Its unrestricted quantum optimality is asymptotic in the stated partial-output regime. The homodyne result covers diffusive quadrature currents with arbitrary predictable phase; its classical filtering reference is connected to the exact quantum source by a controlled relative bound. The observer-count comparison uses a joint weak-drive and small-tolerance limit. These distinctions are part of the result and remain visible in every reading route.
