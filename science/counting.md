# A one-bit displaced-counting receiver

An observer can track the source with one classical bit. The observer displaces the received field so that its present guess would produce no counts, then reverses the guess after each photon count. The exact stationary error follows from two linear correlation equations.

Displacement followed by photon counting is an established optical discrimination idea. Adaptive finite-state monitoring is also established. The [related-work account](../references/related-work.md) attributes those constructions and distinguishes the partial-output error derived here from earlier state-discrimination and pure-ensemble tasks.

## 1. The receiver

Use the [source convention](model.md)

```math
\mathcal L\rho=-i[\Omega X/2,\rho]+\Gamma\mathcal D[Z]\rho.
```

One observer receives the branch $`\sqrt\gamma Z`$, where $`0<\gamma\le\Gamma`$. The controller stores $`g\in\{-1,+1\}`$ and displaces the branch by the real amplitude $`-g\sqrt\gamma`$. Its source jump operator is

```math
J_g=\sqrt\gamma(Z-gI).
```

If the source is in $`|g\rangle`$, the displaced field is dark. If it is in $`|-g\rangle`$, the count intensity is $`4\gamma`$. At a count,

```math
J_g=-2g\sqrt\gamma\,P_{-g},
\qquad P_{-g}=\frac{I-gZ}{2}.
```

The jump projects the source onto $`|-g\rangle`$. Replacing $`g`$ by $`-g`$ then makes the bit agree with that state. Between counts the bit remains fixed. The local oscillator and controller act on the outgoing field only.

The jump interpretation explains the receiver, but the calculation below does not assume a sequence of classical source flips between clicks. Coherent evolution and conditional no-count dynamics remain part of the exact quantum instrument.

## 2. Joint state of the source and stored bit

Let $`\rho_g`$ be the unnormalized source state in the sector with stored bit $`g`$. Then $`\rho_++\rho_-`$ is the unconditional source state, and $`\sum_g\operatorname{Tr}\rho_g=1`$. The block master equation is

```math
\dot\rho_g
=\mathcal L\rho_g
-J_g\rho_gJ_g^\dagger
+J_{-g}\rho_{-g}J_{-g}^\dagger.
```

The negative term removes a count from the old bit sector and the positive term deposits it in the new sector. Summing the two equations gives exactly $`\dot\rho=\mathcal L\rho`$, so the receiver preserves the source dynamics when its record is forgotten.

For real displacement, $`\mathcal D[Z-gI]=\mathcal D[Z]`$. The diagonal no-count generator can therefore also be written as

```math
-i[\Omega X/2,\rho_g]
+(\Gamma-\gamma)\mathcal D[Z]\rho_g
-\frac12\{J_g^\dagger J_g,\rho_g\}.
```

This is the usual positive no-count evolution with the received-channel counts removed. [Complex calibration errors](imperfections.md) require an additional instrument Hamiltonian term; the source-preserving block form remains valid there.

## 3. Exact correlation closure

Define the two real correlations

```math
c_z=\sum_{g=\pm1}g\operatorname{Tr}(Z\rho_g),
\qquad
c_y=\sum_{g=\pm1}g\operatorname{Tr}(Y\rho_g).
```

The terminal guessing error is

```math
e_{\mathrm{null}}(t)
=\sum_g\operatorname{Tr}(P_{-g}\rho_g)
=\frac{1-c_z(t)}2.
```

The Hamiltonian rotates the $`y,z`$ coordinates, and dephasing damps the $`y`$ coordinate at rate $`2\Gamma`$. The count contribution closes because

```math
J_g^\dagger ZJ_g=2\gamma(Z-gI),
\qquad J_g^\dagger YJ_g=0.
```

Relabeling the incoming bit sector after a click gives

```math
\begin{aligned}
\dot c_z&=\Omega c_y+4\gamma(1-c_z),\\
\dot c_y&=-\Omega c_z-2\Gamma c_y.
\end{aligned}
```

These equations hold for every admissible initial joint state. Their homogeneous matrix has characteristic polynomial

```math
u^2+(4\gamma+2\Gamma)u+(8\Gamma\gamma+\Omega^2).
```

Both roots have negative real part for positive $`\Gamma,\gamma`$. The correlations therefore converge to a unique fixed point even without a separate ergodicity assumption for the entire detector record. Setting the derivatives to zero gives

```math
c_z^{\mathrm{ss}}
=\frac{8\Gamma\gamma}{\Omega^2+8\Gamma\gamma},
\qquad
c_y^{\mathrm{ss}}
=-\frac{\Omega}{2\Gamma}c_z^{\mathrm{ss}}.
```

Hence the stationary and long-run mean error are exactly

```math
\boxed{
e_{\mathrm{null}}
=\frac{\Omega^2}{2(\Omega^2+8\Gamma\gamma)}
=\frac{q}{2(1+q)}
=\frac{\delta}{16+2\delta}.
}
```

The result holds at finite drive strength. For $`\delta\to0`$,

```math
e_{\mathrm{null}}=\frac\delta{16}+O(\delta^2).
```

The [quantum converse](quantum_limit.md) proves that the coefficient $`1/16`$ is optimal uniformly over $`0<\gamma/\Gamma\le1/2`$. It does not establish exact optimality of this one-bit receiver for arbitrary finite $`\delta`$. Complete-output access $`\gamma=\Gamma`$ has a separate quantum-memory exception described there.

## 4. Tracking mechanism and its limits

In the weak-drive regime the slow source relaxation corresponds to a classical sign-switch process with leading-order rate $`\lambda=\Omega^2/(4\Gamma)`$. A temporarily wrong nulling guess produces counts at rate $`4\gamma`$, suggesting an error of order $`\lambda/(4\gamma)=\Omega^2/(16\Gamma\gamma)`$. This is useful physical intuition for the exact result. It is not its derivation.

For the ideal pointer states, a click is impossible under the currently nulled sign and therefore resolves the sign without a false alarm. Diffusive homodyne produces overlapping noisy currents under both signs, even with a fixed source. The [homodyne proof](homodyne.md) shows how that distinction produces a logarithm in the optimal causal tracking error of that measurement class.

The ideal receiver uses an exact displacement and an instantaneous response. Phase or amplitude mismatch makes the nominally dark output bright, and dark counts can flip a correct bit. The exact modified error and its accuracy budget are given in [imperfections](imperfections.md). Those formulas concern this receiver, not a universal optimum for all noisy receivers.

## 5. Equal sharing and verification

For $`R`$ equal branches, $`\gamma=\Gamma/R`$, every observer can independently run this receiver. Their marginal stationary errors are

```math
e_{\mathrm{null}}(R)
=\frac{R\Omega^2}{2(R\Omega^2+8\Gamma^2)}.
```

Solving $`e_{\mathrm{null}}(R)\le\epsilon`$ gives the exact attainable count

```math
R_{\mathrm{null}}(\epsilon;\Gamma,\Omega)
=\left\lfloor
\frac{16\Gamma^2}{\Omega^2}\frac\epsilon{1-2\epsilon}
\right\rfloor,
\qquad 0<\epsilon<\frac12.
```

A floor of zero means that this construction cannot meet the tolerance even for one observer. [Observer counts](observer_counts.md) combines this construction with receiver-independent bounds and allows unequal fixed fractions.

The [verification suite](../verification/README.md) constructs the full eight-dimensional linear generator for the two unnormalized density matrices, solves its stationary state without using the correlation formula, and checks the transient closure on random positive block states. These finite numerical checks support the algebra; the closed equations above provide the proof.
