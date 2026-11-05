# The quantum limit for a causal observer

The displaced-counting receiver reaches an error proportional to the inverse information rate in one output branch. This page proves that its leading coefficient is optimal even when the observer can store its entire causal output coherently and make an arbitrary collective measurement. The proof works directly with the driven quantum source; it does not assume that the source has become a classical telegraph process.

The central device is a measurement on the inaccessible output. Its genuine, randomly timed projective events let us give the observer a known source state without changing the observed-output experiment. Between these events, the output states are pure. A binary discrimination bound and a renewal calculation then give a uniform lower bound.

The [model and error criterion](model.md) define the shared task. The [counting receiver](counting.md) attains the bound to leading order, and [observer counts](observer_counts.md) turn the error bounds into limits on output sharing. The ideal construction's calibration and dark-count requirements are treated separately in [imperfections](imperfections.md).

## 1. Model, receiver class, and result

The source is a qubit with the convention

```math
\frac{d\rho}{dt}
=-i\left[\frac{\Omega X}{2},\rho\right]
+\Gamma\mathcal D[Z]\rho,
\qquad
\mathcal D[L]\rho=L\rho L^\dagger
-\frac12\{L^\dagger L,\rho\}.
```

All input fields are independent vacuum fields. The observer receives a branch with coupling $`\sqrt\gamma Z`$; the inaccessible branches have total rate $`\kappa=\Gamma-\gamma`$. Receiver operations act downstream and do not feed back to the source. At time $`t`$, the target is the outcome of a projective $`Z`$ measurement on the source. Earlier output observables commute with this target measurement, so the joint guessing task is well defined.

Let $`e_{\mathrm{all}}(t)`$ be the smallest error when the observer is granted its entire raw output up to $`t`$, an arbitrary ancillary memory, and an arbitrary final measurement. This grants at least the information available to any causal receiver that has already processed or measured its output. A lower bound on $`e_{\mathrm{all}}(t)`$ therefore bounds every such receiver's error at that time. The initial source state may be mixed or correlated with older memory; future vacuum inputs must be independent of that initial state.

For a causal receiver $`\mathcal R`$, let $`e_{\mathcal R}(t)`$ denote its error against the target at time $`t`$. The optimal long-run criterion is

```math
e_{\mathrm Q}
=\inf_{\mathcal R}\limsup_{L\to\infty}
\frac1L\int_0^L e_{\mathcal R}(t)\,dt.
```

Each error in this average refers to a final readout in the experiment stopped at its indicated time. The definition does not introduce repeated projective measurements of the source during operation.

**Theorem.** Suppose

```math
0<\gamma\le\frac\Gamma2,
\qquad
0<\delta:=\frac{\Omega^2}{\Gamma\gamma}<1.
```

For

```math
t\ge 2T,
\qquad
T=\frac{\log(1/\delta)}{4\gamma},
```

every allowed receiver satisfies

```math
\boxed{
e_{\mathrm{all}}(t)
\ge
\frac{\delta}{16}
\left[
1-3\sqrt\delta
-\frac{20}{3}\delta\log^2(1/\delta)
\right].
}
```

The inequality remains valid when its right-hand side is negative. For stationary operation, the [counting construction](counting.md) has exact error

```math
e_{\mathrm{null}}
=\frac{\Omega^2}{2(\Omega^2+8\Gamma\gamma)}
=\frac{\delta}{16+2\delta}.
```

Thus the optimal stationary or long-run error has the uniform asymptotic form

```math
e_{\mathrm Q}
=\frac{\Omega^2}{16\Gamma\gamma}\,[1+o(1)],
\qquad
\delta\longrightarrow0,
\quad 0<\frac\gamma\Gamma\le\frac12.
```

Uniformity includes sequences for which $`\gamma/\Gamma\to0`$ and $`\Omega/\gamma`$ is large. Long-run operation is taken at each fixed parameter triple before this small-$`\delta`$ limit. For $`R\ge2`$ equal output branches, $`\gamma=\Gamma/R`$, so the result covers growing numbers of observers whenever $`\Omega^2R/\Gamma^2\to0`$. It is a marginal statement about each observer's error, not a simultaneous all-observer success theorem. The [homodyne analysis](homodyne.md) gives the corresponding comparison for adaptive quadrature measurements.

## 2. A physical instrument on the inaccessible output

A lower-bound proof may give an observer extra information, provided that doing so preserves the original observed-output and target experiment. Simply measuring $`Z`$ on the source at an arbitrary earlier time would fail this requirement: that measurement can destroy source–output correlations. We instead measure an output which is already inaccessible.

Combine the inaccessible dephasing branches into a single channel with coupling $`\sqrt\kappa Z`$. This is possible by a passive transformation of proportional couplings; the other transformed channels have zero coupling. Split this output equally with vacuum, displace the two resulting outputs by the opposite real amplitudes $`\pm\sqrt{\kappa/2}`$, and count both. The two source jump operators are

```math
L_+=\sqrt{\frac\kappa2}(Z+I)
=\sqrt{2\kappa}\,P_+,
\qquad
L_-=\sqrt{\frac\kappa2}(Z-I)
=-\sqrt{2\kappa}\,P_-,
```

where $`P_\pm=(I\pm Z)/2`$. Their combined intensity is

```math
L_+^\dagger L_++L_-^\dagger L_-=2\kappa I.
```

Their dissipators reproduce exactly the inaccessible dephasing:

```math
\mathcal D[L_+]+\mathcal D[L_-]
=\kappa\mathcal D[Z]
=2\kappa(\Delta_Z-\mathrm{Id}),
\qquad
\Delta_Z(\rho)=\sum_{s=\pm}P_s\rho P_s.
```

Consequently the counting times form a state-independent Poisson process of rate $`2\kappa`$. At each count the source undergoes a projective $`Z`$ measurement. The no-count part from these channels is a scalar survival factor, so after normalization the evolution between counts contains only the Hamiltonian and the observed branch.

This is an operation on the actual inaccessible output, using vacuum ancillary modes and local oscillators. Averaging its record preserves the complete source–observed-output state, including its correlations with the target. The interpretation of different output measurements as different conditional quantum trajectories is standard [2]; the explicit instrument above fixes the operation required here.

## 3. A genuine event screens arbitrary older quantum memory

Let $`M`$ contain all older receiver memory and output, and let $`\rho_{SM}`$ be arbitrary. At one of the genuine events just constructed, condition on the revealed outcome $`s`$. The rank-one identity

```math
(P_s\otimes I_M)\rho_{SM}(P_s\otimes I_M)
=P_s\otimes\langle s|\rho_{SM}|s\rangle
```

shows that the source becomes a known pointer state and factorizes from the older memory. Given the event time and outcome, future vacuum increments are independent of that memory. Older records therefore cannot distinguish subsequent source alternatives once this boundary information has been supplied.

This argument allows arbitrary coherent memory and arbitrary initial correlations. It does not assume that the observer had previously made a classical record. All downstream receiver processing can be included in a final measurement of the raw output and ancillary systems; granting the raw output can only improve the observer's performance.

We first analyze an experiment of deterministic length $`L`$ starting immediately after such a revealed event. Section 8 places this experiment inside an arbitrary observation history.

## 4. Pure interval fields and a finite discrimination experiment

Reveal the times of all inaccessible events in $`(0,L)`$, but initially withhold their outcomes. Include the final target measurement at $`L`$ as the last endpoint. Let the interval lengths be $`d_1,\ldots,d_n`$, with $`\sum_i d_i=L`$.

For one interval, let $`V_\gamma(d)`$ be the source–observed-field isometry generated by the Hamiltonian and the observed coupling, with a vacuum field input. Define unnormalized field vectors

```math
|\phi_{b,a}(d)\rangle
=\langle b|V_\gamma(d)|a\rangle,
\qquad a,b\in\{+,-\}.
```

Conjugating the source by $`X`$ preserves its Hamiltonian and reverses the sign of $`Z`$; a phase rotation by $`\pi`$ of the vacuum field cancels the latter change. This symmetry gives the same endpoint transition probability for either initial sign:

```math
p(d)
=\|\phi_{-,+}(d)\|^2
=\|\phi_{+,-}(d)\|^2,
\qquad
\|\phi_{+,+}(d)\|^2
=\|\phi_{-,-}(d)\|^2=1-p(d).
```

For fixed interval lengths, the indicators of a changed sign at successive endpoints are therefore independent Bernoulli variables with probabilities $`p_i=p(d_i)`$. Conditional on a complete sequence of endpoint outcomes, the interval fields are a tensor product of pure states. This is an exact decomposition of the quantum experiment. A changed endpoint sign is not an assumption about an unmeasured ontic trajectory between endpoints.

Only two interval overlaps are needed:

```math
c(d)=\langle\phi_{+,+}(d)|\phi_{-,+}(d)\rangle,
\qquad
a(d)=\langle\phi_{+,+}(d)|\phi_{-,-}(d)\rangle.
```

Compare no changed endpoint signs with exactly one change, at interval $`k`$. Before $`k`$ their field states coincide. At $`k`$ the overlap is set by $`c(d_k)`$; after $`k`$ it is set by $`a(d_i)`$. The squared overlap of their normalized full field states is

```math
F_k
=\frac{|c(d_k)|^2}{p_k(1-p_k)}
\prod_{i>k}\frac{|a(d_i)|^2}{(1-p_i)^2}.
```

The same formula holds for either revealed initial sign.

### A genie that preserves the zero/one-change ambiguity

Write

```math
P_0=\prod_i(1-p_i),
\qquad
r_i=\frac{p_i}{1-p_i},
\qquad
R_0=\sum_i r_i.
```

The probability of exactly one change is $`P_1=P_0R_0`$. Grant the following additional classical information:

1. If there are at least two changes, reveal the final answer. This branch contributes zero error.
2. Otherwise reveal an index $`K`$. With one change, reveal its actual index. With no changes, independently draw $`K=k`$ with probability $`r_k/R_0`$.

In the second case, the conditional index distribution is the same under the no-change and one-change alternatives. For a particular index $`k`$, their unnormalized prior weights are

```math
A_k=P_0\frac{r_k}{R_0},
\qquad
B_k=P_0r_k.
```

These weights include the probability of receiving that genie message. They must not be replaced by equal priors.

For two normalized pure states with squared overlap $`F`$ and unnormalized weights $`A,B`$, binary quantum hypothesis testing [1] gives

```math
E(A,B,F)
=\frac{A+B-\sqrt{(A+B)^2-4ABF}}2
\ge\frac{ABF}{A+B}.
```

The inequality follows directly by rationalizing the square root. Summing over the messages $`K=k`$ gives

```math
e(d_1,\ldots,d_n)
\ge
\frac{P_0}{1+R_0}
\sum_k
\frac{|c(d_k)|^2}{(1-p_k)^2}
\prod_{i>k}\frac{|a(d_i)|^2}{(1-p_i)^2}.
```

The left side may be taken as the optimal error before any of these additional messages: extra information can only lower the optimal error. Zero-probability alternatives are removed or treated by continuity.

### A useful relaxation

Define

```math
S=\sum_k |c(d_k)|^2\prod_{i>k}|a(d_i)|^2,
\qquad
s=\sum_i p_i.
```

Dropping the reciprocal denominator factors lowers the right side. Moreover, $`S\le s`$, because $`|c(d)|^2\le p(d)(1-p(d))`$ and $`|a(d)|\le1`$. If $`s<1/2`$, then

```math
P_0\ge1-s,
\qquad
R_0\le\frac{s}{1-s},
\qquad
\frac{P_0}{1+R_0}\ge(1-s)^2\ge1-2s.
```

For $`s\ge1/2`$, the last inequality remains true because its right side is nonpositive. Hence the exact finite-partition bound implies

```math
e(d_1,\ldots,d_n)\ge S-2s^2.
```

## 5. Local interval estimates

The interval quantities can be calculated from the reduced channel without representing its infinite-dimensional field. In the $`y,z`$ Bloch coordinates the generator is

```math
M=\begin{pmatrix}-2\gamma&-\Omega\\ \Omega&0\end{pmatrix}.
```

Starting from $`|+\rangle`$, the Bloch vector obeys $`y(0)=0`$, $`z(0)=1`$, and

```math
p(d)=\frac{1-z(d)}2,
\qquad
c(d)=\frac{i\,y(d)}2.
```

The integral equations and $`|z(u)|\le1`$ give

```math
|y(u)|\le|\Omega|u,
\qquad
|1-z(u)|\le\frac{\Omega^2u^2}{2},
\qquad
p(d)\le\frac{\Omega^2d^2}{4}.
```

Replacing $`z(u)`$ by $`1`$ in the integral for $`y(d)`$ gives a first-order term with a uniform remainder:

```math
y(d)
=-\frac{\Omega}{2\gamma}(1-e^{-2\gamma d})+\mathcal R_y(d),
\qquad
|\mathcal R_y(d)|\le\frac{|\Omega|^3d^3}{6}.
```

Set

```math
c_0(d)=\frac{|\Omega|}{4\gamma}(1-e^{-2\gamma d}).
```

Since both $`|c(d)|`$ and $`c_0(d)`$ are at most $`|\Omega|d/2`$,

```math
\bigl||c(d)|^2-c_0(d)^2\bigr|
\le\frac{\Omega^4d^4}{12}.
```

For the other overlap, apply the reduced interval channel to $`|+\rangle\langle-|=(X+iY)/2`$. The $`X`$ component decays as $`e^{-2\gamma d}`$, while the $`Y`$ component evolves under $`M`$. Thus

```math
a(d)=\frac{e^{-2\gamma d}+(e^{Md})_{yy}}2.
```

For the Bloch initial condition $`y(0)=1,z(0)=0`$, one has $`|z(u)|\le|\Omega|u`$. Its integral equation therefore gives

```math
|a(d)-e^{-2\gamma d}|\le\frac{\Omega^2d^2}{4},
\qquad
\bigl||a(d)|^2-e^{-4\gamma d}\bigr|
\le\frac{\Omega^2d^2}{2}.
```

All these estimates hold for every nonnegative interval length. They expand only over individual intervals between lost-output events, whose scale is set by $`\kappa`$. They do not require $`|\Omega|L`$ or $`|\Omega|/\gamma`$ to be small.

Define the comparison sum

```math
S_0=\sum_k c_0(d_k)^2
\exp\!\left[-4\gamma\sum_{i>k}d_i\right].
```

For products of numbers in $`[0,1]`$, the absolute difference of the products is at most the sum of the absolute differences of their factors. Using the two overlap estimates and $`c_0(d_k)^2\le\Omega^2d_k^2/4`$ therefore gives

```math
|S-S_0|
\le\Omega^4\left[
\frac1{12}\sum_i d_i^4
+\frac18\sum_{k<i}d_k^2d_i^2
\right]
\le\frac{\Omega^4}{12}\left(\sum_i d_i^2\right)^2.
```

Also,

```math
2s^2\le\frac{\Omega^4}{8}\left(\sum_i d_i^2\right)^2.
```

The resulting finite-partition estimate is

```math
\boxed{
e(d_1,\ldots,d_n)
\ge S_0
-\frac5{24}\Omega^4\left(\sum_i d_i^2\right)^2.
}
```

## 6. Poisson averaging of the remainder

The interior endpoints form a Poisson process of rate $`2\kappa`$ on $`[0,L]`$. The last interval is truncated at the final target measurement. Let $`A(u)`$ be the age since the latest Poisson event, or since the initial boundary if no event has yet occurred. Then

```math
\sum_i d_i^2=2\int_0^L A(u)\,du.
```

For each $`u`$, $`A(u)`$ is stochastically dominated by an exponential variable of rate $`2\kappa`$, so

```math
\mathbb E[A(u)^2]\le\frac{1}{2\kappa^2}.
```

Cauchy–Schwarz now yields

```math
\mathbb E\left[\left(\sum_i d_i^2\right)^2\right]
\le4L\int_0^L\mathbb E[A(u)^2]\,du
\le\frac{2L^2}{\kappa^2}.
```

There is no cutoff on the largest interval and no assumption excluding rare long intervals.

## 7. The exact renewal coefficient

Let $`t_i=\sum_{j\le i}d_j`$, including $`t_n=L`$, and define

```math
f(d)=(1-e^{-2\gamma d})^2,
\qquad
F(L)=\mathbb E\!\left[
\sum_i f(d_i)e^{-4\gamma(L-t_i)}
\right].
```

The leading sum obeys $`\mathbb E S_0=\Omega^2F(L)/(16\gamma^2)`$. We compute $`F`$ exactly, including the truncated last interval.

Write $`\nu=2\kappa`$ and let $`h(L)=\mathbb E f(A(L))`$. The Poisson age distribution has an atom at $`L`$ when there has been no event, and an exponential density on $`(0,L)`$. Therefore

```math
h(L)=e^{-\nu L}f(L)
+\nu\int_0^L e^{-\nu u}f(u)\,du.
```

The terminal interval contributes $`h(L)`$. The mean sum over completed intervals is the event intensity times the mean reward at an event, discounted from that event to $`L`$. Hence

```math
F(L)=h(L)+\nu\int_0^L h(u)e^{-4\gamma(L-u)}\,du.
```

For the Laplace transform $`\widetilde g(s)=\int_0^\infty e^{-sL}g(L)\,dL`$,

```math
\widetilde f(s)
=\frac1s-\frac2{s+2\gamma}+\frac1{s+4\gamma}
=\frac{8\gamma^2}{s(s+2\gamma)(s+4\gamma)}.
```

It follows that

```math
\widetilde h(s)
=\left(1+\frac\nu s\right)\widetilde f(s+\nu),
\qquad
\widetilde F(s)
=\left(1+\frac\nu{s+4\gamma}\right)\widetilde h(s)
=\frac{8\gamma^2}{s(s+4\gamma)(s+2\Gamma)}.
```

Equivalently, for independent exponential variables $`X\sim\operatorname{Exp}(4\gamma)`$ and $`Y\sim\operatorname{Exp}(2\Gamma)`$,

```math
F(L)=\frac\gamma\Gamma\Pr(X+Y\le L),
\qquad
\boxed{
\mathbb E S_0
=\frac{\Omega^2}{16\Gamma\gamma}\Pr(X+Y\le L).
}
```

At $`\Gamma=2\gamma`$, this probability is $`1-(1+2\Gamma L)e^{-2\Gamma L}`$. Otherwise it is

```math
\Pr(X+Y\le L)
=1-\frac{\Gamma e^{-4\gamma L}-2\gamma e^{-2\Gamma L}}
{\Gamma-2\gamma}.
```

For $`\Gamma\ge2\gamma`$, requiring both $`X\le L/2`$ and $`Y\le L/2`$ gives the convenient lower bound

```math
\Pr(X+Y\le L)
\ge1-e^{-2\gamma L}-e^{-\Gamma L}
\ge1-2e^{-2\gamma L}.
```

Combining the leading term and the remainder, a known pointer input followed for length $`L`$ has optimal error at least

```math
e_{\mathrm{pointer}}(L)
\ge
\frac{\Omega^2}{16\Gamma\gamma}(1-2e^{-2\gamma L})
-\frac5{12}\frac{\Omega^4L^2}{\kappa^2}.
```

The factor $`\Gamma`$ in the denominator emerges from this exact renewal average. Omitting the terminal interval would change that coefficient.

## 8. Inserting the bound into an arbitrary past history

Fix a terminal time $`t\ge2T`$. Start a genie window at $`t-2T`$ and consider the first lost-output event after this boundary.

If no event occurs by $`t-T`$, reveal the final answer, making this branch error-free. Its probability is $`e^{-2\kappa T}`$. Otherwise reveal the first event's time and outcome. Section 3 makes the source a known pointer state independent of all older quantum memory. The remaining duration $`L`$ is between $`T`$ and $`2T`$; subsequent event times are a fresh rate-$`2\kappa`$ Poisson process.

Reveal those subsequent times and apply the finite-partition genie. The preceding pointer-input bound is uniform over $`L\in[T,2T]`$ after taking $`L=T`$ in the positive term and $`L=2T`$ in the negative term. Hence

```math
e_{\mathrm{all}}(t)
\ge
(1-e^{-2\kappa T})
\left[
\frac{\Omega^2}{16\Gamma\gamma}(1-2e^{-2\gamma T})
-\frac53\frac{\Omega^4T^2}{\kappa^2}
\right].
```

The right side may be replaced by zero when it is negative. This is the useful finite-window bound before a particular $`T`$ is chosen.

For $`T=\log(1/\delta)/(4\gamma)`$ and $`\kappa\ge\gamma`$,

```math
e^{-2\gamma T}=\sqrt\delta,
\qquad
e^{-2\kappa T}\le\sqrt\delta,
\qquad
\kappa\ge\frac\Gamma2.
```

Also,

```math
\frac53\frac{\Omega^4T^2}{\kappa^2}
\le\frac5{12}\delta^2\log^2(1/\delta).
```

Whenever the resulting positive expression is informative, substitute these estimates and use $`(1-\sqrt\delta)(1-2\sqrt\delta)\ge1-3\sqrt\delta`$. This gives

```math
e_{\mathrm{all}}(t)
\ge
\frac\delta{16}
\left[1-3\sqrt\delta
-\frac{20}{3}\delta\log^2(1/\delta)\right].
```

If the final right side is nonpositive, the same assertion follows from nonnegativity of error. This proves the theorem over the full stated parameter range.

## 9. Why the bound applies to continuous operation

The lower bound is proved for a relaxed experiment in which a receiver can preserve all available coherence until a chosen terminal time. A receiver that must keep reporting guesses has already committed to particular operations on its older output. At any chosen time, its memory and record arise from a channel applied to the same raw output; it cannot outperform the relaxed experiment. The bound therefore holds at every sufficiently late reporting time for every such receiver.

In particular it bounds stationary errors, limiting errors when those exist, and long-run time-averaged errors. The finite initial interval before $`2T`$ contributes a vanishing fraction to a long-run average. The one-bit nulling receiver is usable indefinitely and has the stationary upper bound stated in Section 1. Thus the leading coefficient is attainable in continuous operation, even though the converse allows a more powerful terminal measurement.

The assumptions that make this conclusion possible are partial output access, independent vacuum inputs, and the absence of feedback to the source. Unlimited downstream computation, local oscillators, and quantum memory are already included in the lower-bound receiver class.

## 10. Complete output access is a genuine exception

The restriction to $`\gamma\le\Gamma/2`$ must not be silently extended to $`\gamma=\Gamma`$. Consider a known pure initial source state and collection of every output mode. At a terminal time, the joint source–output state is pure and can be written

```math
|\Psi(t)\rangle
=|+\rangle|f_+(t)\rangle+|-\rangle|f_-(t)\rangle.
```

The field vectors are unnormalized. Their overlap is the source coherence, up to complex conjugation. The minimum error of an output-only measurement predicting final $`Z`$ is exactly

```math
e_{\mathrm{full}}(t)
=\frac{1-\sqrt{1-4|\rho_{+-}(t)|^2}}2.
```

For $`\Omega\ne0`$ and $`\Gamma>0`$, the unconditional source approaches $`I/2`$, so $`\rho_{+-}(t)\to0`$ and $`e_{\mathrm{full}}(t)\to0`$. The two conditional output vectors become orthogonal even though the source itself is maximally mixed. By contrast, the nulling receiver's stationary error is positive at fixed nonzero $`\Omega`$.

This counterexample concerns one terminal collective measurement. It does not supply a continuously reusable zero-error readout. It shows why a positive converse obtained by relaxing to an all-past terminal measurement cannot cover complete collection. With inaccessible output, the genuine projective-event instrument provides the valid memory-screening step used above.

## 11. Verification and imported ingredients

Run the numerical checks from the repository root:

```bash
python verification/verify_quantum_limit.py
```

The script constructs interval channels independently in Liouville space, obtains an equivalent pure-output representation from their Choi matrices, and checks the overlap identities and interval estimates. It also checks the finite-partition genie weights against the exact binary Helstrom expression and compares direct Poisson-age quadrature with the renewal formula. It reports its sample counts, residuals, and any violations; a failed check returns a nonzero exit status.

These finite calculations check conventions, factors, and implementations. They do not establish the uniform theorem, the continuum-output model, or the validity of the genie. Those statements follow from the argument on this page.

The standard imported ingredients are binary minimum-error discrimination [1] and the connection between output measurements and quantum trajectories [2]. The specific lost-output instrument, its role in screening arbitrary receiver memory, and the quantitative interval and renewal estimates are explicit above.

1. C. W. Helstrom, “Quantum detection and estimation theory,” *Journal of Statistical Physics* **1**, 231–252 (1969). [DOI: 10.1007/BF01007479](https://doi.org/10.1007/BF01007479).
2. H. M. Wiseman and G. J. Milburn, “Interpretation of quantum jump and diffusion processes illustrated on the Bloch sphere,” *Physical Review A* **47**, 1652 (1993). [DOI: 10.1103/PhysRevA.47.1652](https://doi.org/10.1103/PhysRevA.47.1652).
