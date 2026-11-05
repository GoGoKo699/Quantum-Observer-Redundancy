# Diffusive homodyne with adaptive phase

A weak output branch can be measured continuously by choosing a field quadrature and processing its noisy current. This page proves that allowing the quadrature to depend on the complete past record does not remove the logarithmic tracking penalty in the many-observer limit. The proof starts from the exact driven-qubit filter and bounds its error relative to a classical Wonham filter; it does not assume that the quantum output is a telegraph field.

The [model and error criterion](model.md) fix the source, the received branch and the terminal observable. The classical and quantum filtering equations used below are established ingredients, attributed in [classical filtering](../references/related-work.md#classical-filtering) and [continuous quantum measurement](../references/related-work.md#continuous-quantum-measurement). The finite-parameter comparison proved here is the step connecting those ingredients to this source.

## 1. Measurement class and result

The source obeys

```math
\mathcal L\rho=-i[\Omega X/2,\rho]+\Gamma\mathcal D[Z]\rho,
\qquad
\mathcal D[Z]\rho=Z\rho Z-\rho.
```

Assume $`\Gamma>0`$, $`\Omega>0`$, and a received vacuum output channel with coupling $`\sqrt{\gamma}Z`$, where $`0<\gamma\le\Gamma`$. Define

```math
\eta=\frac{\gamma}{\Gamma},
\qquad
r=\frac{\Omega}{2\Gamma},
\qquad
q=\frac{r^2}{2\eta}=\frac{\Omega^2}{8\Gamma\gamma},
\qquad
\tau=2\Gamma t.
```

The receiver measures a diffusive quadrature current. Its local-oscillator phase $`\theta_\tau`$ may be any predictable function of its complete past classical record and independent classical randomness. It may use arbitrary causal classical processing to choose its terminal bit. Predictability means that the phase used for an infinitesimal output interval is selected before that interval's new innovation is observed.

This class includes unlimited classical controller memory. Its measurement operation is the quadrature-current diffusion specified in Section 4. Finite-local-oscillator photon counting, retained quantum field modes and general Gaussian preprocessing are separate measurement classes. This distinction matters because some earlier literature uses “adaptive homodyne” for a displaced-counting construction; the [related-work account](../references/related-work.md#continuous-quantum-measurement) explains that terminology.

Write the conditional state as

```math
\rho_\tau=\frac{I+x_\tau X+y_\tau Y+z_\tau Z}{2}.
```

The optimal bit from this record predicts the sign of $`z_\tau`$. Its conditional error against an instantaneous projective $`Z`$ outcome is

```math
h(z_\tau)=\frac{1-|z_\tau|}{2}.
```

For a phase policy $`\theta`$, let

```math
\overline e_\theta(L)=\frac1L\int_0^L\mathbb E\,h(z_\tau)\,d\tau.
```

A constant rescaling of time leaves the long-run average unchanged. The infimum of $`\limsup_{L\to\infty}\overline e_\theta(L)`$ over the allowed phase policies will be denoted $`e_{\mathrm H}^{\mathrm{opt}}(r,\eta)`$. Any other terminal decision rule has error at least the conditional Bayes error used in this definition.

**Theorem: uniform relative homodyne comparison.** Put

```math
A=1-r^2-\eta,
\qquad
B=r^2+2\eta,
\qquad
C=\eta\left(1+\frac{\eta}{(1-\eta)^2}\right),
```

and suppose $`A>0`$. Define

```math
T(r,\eta)=\frac{B+\sqrt{B^2+4A\eta}}{2A},
\qquad
T_{\mathrm{ad}}(r,\eta)=\frac{B+\sqrt{B^2+4AC}}{2A}.
```

Let $`e_{\mathrm W}(q)`$ be the exact Wonham error derived in Section 2. For every allowed phase policy and every initial qubit state,

```math
\liminf_{L\to\infty}\overline e_\theta(L)
\ge e_{\mathrm W}(q)\bigl[1-T_{\mathrm{ad}}(r,\eta)\bigr].
```

For the real quadrature $`\theta_\tau=0`$,

```math
\limsup_{L\to\infty}
\left|\overline e_0(L)-e_{\mathrm W}(q)\right|
\le e_{\mathrm W}(q)T(r,\eta).
```

Consequently,

```math
e_{\mathrm W}(q)\bigl[1-T_{\mathrm{ad}}(r,\eta)\bigr]
\le e_{\mathrm H}^{\mathrm{opt}}(r,\eta)
\le e_{\mathrm W}(q)\bigl[1+T(r,\eta)\bigr].
```

The same statements hold for stationary errors whenever the corresponding process has a stationary law. They require neither a stationary controller nor uniqueness of the quantum filter's stationary law. A negative lower bound is simply uninformative; the asymptotic regime below has $`T_{\mathrm{ad}}\to0`$.

## 2. The classical Wonham error

### 2.1 Posterior dynamics

Consider a classical signal $`S_t\in\{-1,+1\}`$ that changes sign at rate $`\lambda>0`$ in each state, with observation

```math
dY_t=aS_t\,dt+dB_t,
\qquad a>0,
```

where $`B_t`$ is a standard Brownian motion independent of the signal. If $`m_t=\mathbb E[S_t\mid Y_{[0,t]}]`$, the two-state Wonham filter is

```math
dm_t=-2\lambda m_t\,dt
+a(1-m_t^2)\,dW_t,
\qquad
dW_t=dY_t-am_t\,dt.
```

Here $`W_t`$ is Brownian motion in the observation filtration. One way to obtain the equation is to evolve unnormalized posterior weights:

```math
\begin{aligned}
d\xi_+&=\lambda(\xi_--\xi_+)\,dt+a\xi_+\,dY_t,\\
d\xi_-&=\lambda(\xi_+-\xi_-)\,dt-a\xi_-\,dY_t.
\end{aligned}
```

The transition terms update the two-state prior, while the observation terms update its likelihood. Itô's quotient rule applied to $`m=(\xi_+-\xi_-)/(\xi_++\xi_-)`$ gives the displayed normalized equation. The finite-state filtering construction is due to [Wonham](../references/related-work.md#classical-filtering).

In time $`s=2\lambda t`$, and with $`q=2\lambda/a^2`$, the posterior diffusion has generator

```math
\mathcal A_q f(z)=-z f'(z)+a_q(z)f''(z),
\qquad
a_q(z)=\frac{(1-z^2)^2}{2q},
\qquad -1\le z\le1.
```

The symbol $`a_q`$ denotes the generator coefficient; it is distinct from the physical observation amplitude $`a`$ above.

### 2.2 Invariant law and uniqueness

The diffusion coefficients are Lipschitz on the compact interval. The drift points inward at either endpoint and the diffusion coefficient vanishes there, so the interval is invariant and the process has a Feller semigroup.

There is also an explicit contraction. Couple solutions $`M_s^+`$ and $`M_s^-`$ with ordered initial values using the same Brownian motion. Their difference $`D_s=M_s^+-M_s^-`$ satisfies

```math
dD_s=-D_s\,ds
-\frac{M_s^++M_s^-}{\sqrt q}D_s\,dW_s.
```

Its stochastic-exponential solution stays nonnegative. The coefficient in the stochastic exponential is bounded for fixed $`q>0`$, so that exponential is a true martingale on every finite time interval. Therefore

```math
\mathbb E D_s=e^{-s}D_0.
```

This gives Wasserstein contraction of order one at rate one. Compactness gives an invariant law; contraction makes it unique and implies

```math
\mathrm{Lip}(P_s g)\le e^{-s}\mathrm{Lip}(g)
```

for its semigroup $`P_s`$.

Solving the zero-current equation $`(a_qp_q)'=-zp_q`$ gives the invariant density

```math
p_q(z)=\frac1{\mathcal Z(q)}
\frac{\exp[-q/(1-z^2)]}{(1-z^2)^2},
\qquad -1\lt z\lt 1.
```

The density is integrable, and $`a_qp_q`$ vanishes faster than any power at the endpoints. Integration by parts verifies stationarity on twice continuously differentiable test functions; uniqueness identifies this density with the invariant law.

### 2.3 Normalization and exact error

Set $`z=\tanh x`$. Then

```math
\begin{aligned}
\mathcal Z(q)
&=\int_{-\infty}^{\infty}\cosh^2x\,e^{-q\cosh^2x}\,dx\\
&=\frac{e^{-q/2}}2
\left[K_0(q/2)+K_1(q/2)\right].
\end{aligned}
```

The last equality uses the standard modified-Bessel representation
$`K_\nu(u)=\int_0^\infty e^{-u\cosh v}\cosh(\nu v)\,dv`$
for $`u>0`$; see [NIST DLMF, equation 10.32.9](https://dlmf.nist.gov/10.32.E9).

The unnormalized absolute first moment is particularly simple:

```math
\begin{aligned}
\int_{-1}^1
\frac{|z|\,e^{-q/(1-z^2)}}{(1-z^2)^2}\,dz
&=\int_1^\infty e^{-qu}\,du\\
&=\frac{e^{-q}}q.
\end{aligned}
```

Thus the exact stationary Bayes error is

```math
e_{\mathrm W}(q)
=\frac12\left[1-\frac{e^{-q}}{q\mathcal Z(q)}\right],
\qquad 0\lt e_{\mathrm W}(q)\lt\frac12.
```

For stable numerical evaluation, write $`K_\nu^{\mathrm{sc}}(u)=e^uK_\nu(u)`$. Then

```math
e_{\mathrm W}(q)
=\frac12\left[
1-\frac{2}{
q\{K_0^{\mathrm{sc}}(q/2)+K_1^{\mathrm{sc}}(q/2)\}}
\right].
```

The small-argument series for $`K_0`$ and $`K_1`$ give

```math
q\mathcal Z(q)
=1+\frac q2\left[\log\frac4q-\gamma_{\mathrm E}-1\right]
+O\!\left(q^2\log\frac1q\right).
```

Using $`e^{-q}=1-q+O(q^2)`$ in the exact error yields

```math
e_{\mathrm W}(q)
=\frac q4\left[\log\frac4q+1-\gamma_{\mathrm E}\right]
+O\!\left(q^2\log^2\frac1q\right),
\qquad q\downarrow0.
```

Here $`\gamma_{\mathrm E}`$ is Euler's constant. The Bessel series are recorded in [NIST DLMF, equations 10.31.1–10.31.2](https://dlmf.nist.gov/10.31). This logarithm belongs to the classical causal filtering problem.

## 3. A convex Poisson solution with a sharp gradient bound

The comparison with the quantum source needs more than convergence of an effective drift. It needs a Poisson solution whose gradient is as small as the error being estimated.

**Lemma.** For every $`q>0`$, the equation

```math
\mathcal A_q f_q=h-e_{\mathrm W}(q)
```

has an even, convex solution, unique up to an additive constant, in $`C^2([-1,1])`$. It satisfies

```math
f_q'(1)=e_{\mathrm W}(q),
\qquad
f_q'(-1)=-e_{\mathrm W}(q),
\qquad
\|f_q'\|_\infty=e_{\mathrm W}(q),
\qquad
f_q''\ge0.
```

The endpoint second derivatives also exist:

```math
f_q''(1)=f_q''(-1)=\frac12-e_{\mathrm W}(q).
```

### 3.1 Construction and the Poisson equation

For brevity write $`e=e_{\mathrm W}(q)`$, $`p=p_q`$ and $`a_q=a_q(z)`$. On the open interval define

```math
f_q'(z)=
\frac{\displaystyle\int_{-1}^{z}(h(u)-e)p(u)\,du}
{a_q(z)p(z)}.
```

The total numerator integral is zero because $`e=\int hp`$. Symmetry makes the numerator odd and the denominator even, so $`f_q'`$ is odd. Integrating it gives an even function after choosing an additive constant.

The identity $`(a_qp)'=-zp`$ implies

```math
(a_qp f_q')'=(h-e)p,
```

and hence $`a_q f_q''-zf_q'=h-e`$ in the interior. Since $`h`$ is continuous and $`a_q>0`$ there, the constructed function is twice continuously differentiable throughout the open interval, including at $`z=0`$. The kink in the first derivative of $`h`$ introduces no local-time term.

### 3.2 Convexity and endpoint regularity

For $`0\lt z\lt 1`$, define three positive integrals:

```math
\begin{aligned}
L(z)&=\int_z^1 p(u)\,du,\\
M(z)&=\int_z^1 up(u)\,du=a_q(z)p(z),\\
J(z)&=M(z)-zL(z)=\int_z^1(u-z)p(u)\,du.
\end{aligned}
```

Using $`h(u)=(1-u)/2`$ on this half-interval gives

```math
f_q'(z)=\frac12+\left(e-\frac12\right)\frac{L(z)}{M(z)}.
```

Differentiating the ratio yields

```math
f_q''(z)=
\left(\frac12-e\right)\frac{p(z)J(z)}{M(z)^2}
\ge0.
```

Evenness extends convexity to the whole interval. Moreover, $`L/M\to1`$ as $`z\uparrow1`$, either by bounding $`u`$ between $`z`$ and $`1`$ in the defining integrals or by l'Hôpital's rule. Thus $`f_q'(1)=e`$.

To check the second derivative, observe that

```math
\frac{pJ}{M^2}=\frac{J}{a_q^2p},
\qquad
J'=-L,
\qquad
(a_q^2p)'=M(a_q'-z).
```

Both $`J`$ and $`a_q^2p`$ vanish at $`1`$, and $`a_q'(z)\to0`$. Moreover, $`a_q'(z)<0`$ on $`(0,1)`$, so the derivative $`M(a_q'-z)`$ never vanishes there. A final l'Hôpital limit gives

```math
\lim_{z\uparrow1}\frac{J(z)}{a_q(z)^2p(z)}
=
\lim_{z\uparrow1}
\frac{L(z)}{M(z)[z-a_q'(z)]}
=1.
```

Therefore $`f_q''(1)=1/2-e`$. Symmetry gives both derivative limits at $`-1`$. This proves the claimed $`C^2`$ extension and, by convexity, the sharp gradient bound.

These regularity statements are sufficient for all later Itô calculations. For fixed $`q>0`$, extend $`f_q`$ as a $`C^2`$ function to an open neighborhood of $`[-1,1]`$ by matching its endpoint value and first two derivatives. The quantum coordinate always lies in the interval, so ordinary Itô's formula applies, including at endpoints. All relevant derivatives are bounded for that fixed $`q`$. No unspecified boundary localization or exchange of singular limits is required.

### 3.3 Semigroup interpretation

Choose the additive constant so that $`\int f_qp_q=0`$. Itô's formula for the classical diffusion and the contraction in Section 2 give

```math
f_q(z)
=-\int_0^\infty
\left[P_s h(z)-e_{\mathrm W}(q)\right]\,ds.
```

The integral converges uniformly: contraction bounds the absolute integrand by
$`e^{-s}\mathrm{Lip}(h)\int|z-u|p_q(u)\,du\le e^{-s}`$.

Convexity also has a decision-theoretic explanation. For fixed $`s`$, $`P_s h(z)`$ is the optimal error for deciding the terminal classical sign when the initial prior for $`+1`$ is $`(1+z)/2`$. Every fixed decision rule has risk affine in that prior. The infimum over decision rules is concave, making the negative time integral convex. The explicit calculation above supplies the endpoint values needed for the relative estimate.

## 4. The exact quantum diffusion

Let $`c_\tau=\cos\theta_\tau`$ and $`s_\tau=\sin\theta_\tau`$. The measured current and conditional state satisfy

```math
\begin{aligned}
dY_t&=2\sqrt\gamma\,c_t z_t\,dt+dW_t,\\
d\rho_t&=\mathcal L\rho_t\,dt
+\sqrt\gamma\left[
c_t(Z\rho_t+\rho_t Z-2z_t\rho_t)
-i s_t[Z,\rho_t]
\right]dW_t.
\end{aligned}
```

These are the homodyne innovations equations for a Hermitian output coupling. Their measurement-theoretic derivation is part of established [quantum filtering](../references/related-work.md#continuous-quantum-measurement). Substitution of the Bloch representation gives the exact stochastic equations

```math
\begin{aligned}
dx&=-2\Gamma x\,dt
+2\sqrt\gamma(-czx-sy)\,dW_t,\\
dy&=(-\Omega z-2\Gamma y)\,dt
+2\sqrt\gamma(-czy+sx)\,dW_t,\\
dz&=\Omega y\,dt
+2\sqrt\gamma\,c(1-z^2)\,dW_t.
\end{aligned}
```

A reversed phase convention changes both occurrences of $`s`$ in sign and leaves the proof unchanged. There is no Hamiltonian feedback to the source.

Set

```math
u=\frac xr,\qquad w=\frac yr,\qquad v=w+z.
```

In time $`\tau`$, Brownian rescaling gives

```math
\begin{aligned}
du&=-u\,d\tau+\sqrt{2\eta}(-zcu-sw)\,dW_\tau,\\
dw&=-(z+w)\,d\tau+\sqrt{2\eta}(-zcw+su)\,dW_\tau,\\
dz&=r^2w\,d\tau+\sqrt{2\eta}\,c(1-z^2)\,dW_\tau,\\
dv&=-[(1-r^2)v+r^2z]\,d\tau
+\sqrt{2\eta}[c(1-zv)+su]\,dW_\tau.
\end{aligned}
```

All equations hold for predictable, history-dependent phases. For each fixed $`r>0`$, the physical Bloch ball gives uniform bounds on $`u,w,v`$. The scaled coordinates can grow as $`r\downarrow0`$, but they are bounded when taking the long-time limit for a fixed source.

## 5. Uniform moment estimates

For any integrable process $`F_\tau`$, write

```math
\langle F\rangle_L=\frac1L\int_0^L\mathbb E F_\tau\,d\tau.
```

The following estimates apply directly to these time averages. In a stationary law they are the same estimates with the endpoint terms set to zero.

### 5.1 Real quadrature

For $`c=1`$ and $`s=0`$, the last equation in Section 4 becomes

```math
dv=-[(1-r^2)v+r^2z]\,d\tau
+\sqrt{2\eta}(1-zv)\,dW_\tau.
```

Itô's formula, $`|z|\le1`$ and Cauchy–Schwarz give

```math
\frac{d}{d\tau}\mathbb E v^2
\le -2A\,\mathbb E v^2
+2B\sqrt{\mathbb E v^2}
+2\eta.
```

Writing $`X_L=\langle v^2\rangle_L`$, integrating and applying Cauchy–Schwarz in time yields

```math
A X_L
\le B\sqrt{X_L}+\eta+\frac{\mathbb E v_0^2}{2L}.
```

The negative terminal contribution has been discarded. Since $`A>0`$, the positive root of this quadratic inequality implies

```math
\limsup_{L\to\infty}\sqrt{X_L}\le T(r,\eta).
```

### 5.2 Arbitrary predictable phase

First set $`V=u^2+w^2`$. The two diffusion coefficients for $`(u,w)`$ are obtained by applying

```math
\sqrt{2\eta}
\begin{pmatrix}
-zc&-s\\
s&-zc
\end{pmatrix}
```

to $`(u,w)`$. Their sum of squares is
$`2\eta(z^2c^2+s^2)V\le2\eta V`$. Hence

```math
\frac{d}{d\tau}\mathbb E V
\le-2(1-\eta)\mathbb E V+2\mathbb E|w|.
```

After integration,

```math
(1-\eta)\langle V\rangle_L
\le\sqrt{\langle V\rangle_L}
+\frac{\mathbb E V_0}{2L}.
```

Because $`A>0`$ implies $`\eta<1`$, this gives

```math
\limsup_{L\to\infty}\langle V\rangle_L
\le\frac1{(1-\eta)^2}.
```

Next, $`(zcu+sw)^2\le u^2+w^2=V`$. The equation for $`u^2`$ therefore gives

```math
\langle u^2\rangle_L
\le\eta\langle V\rangle_L+\frac{\mathbb E u_0^2}{2L},
\qquad
\limsup_{L\to\infty}\langle u^2\rangle_L
\le\frac{\eta}{(1-\eta)^2}.
```

Finally use

```math
[c(1-zv)+su]^2\le(1-zv)^2+u^2
```

in the equation for $`v^2`$. With $`X_L=\langle v^2\rangle_L`$,

```math
A X_L
\le B\sqrt{X_L}
+\eta\left[1+\langle u^2\rangle_L\right]
+\frac{\mathbb E v_0^2}{2L}.
```

Taking a subsequence on which $`X_L`$ approaches its limsup, and using the preceding bound on $`\langle u^2\rangle_L`$, yields

```math
\limsup_{L\to\infty}\sqrt{X_L}
\le T_{\mathrm{ad}}(r,\eta).
```

Every inequality is independent of the phase policy. In particular, there is no Markov or finite-memory assumption on its classical controller.

## 6. Comparing the exact error with the Wonham error

Apply Itô's formula to the $`C^2`$ function $`f_q(z_\tau)`$. Since $`q=r^2/(2\eta)`$, the exact generator acting on this function is

```math
\begin{aligned}
r^2w f_q'(z)+\eta c^2(1-z^2)^2f_q''(z)
&=r^2\left[w f_q'(z)+c^2a_q(z)f_q''(z)\right]\\
&=r^2\left[
h(z)-e_{\mathrm W}(q)
+vf_q'(z)
-(1-c^2)a_q(z)f_q''(z)
\right].
\end{aligned}
```

All stochastic integrals have zero expectation on finite time intervals: the state space is bounded and, for fixed parameters, so are the derivatives of $`f_q`$. After integrating and dividing by $`r^2L`$,

```math
\begin{aligned}
\overline e_\theta(L)-e_{\mathrm W}(q)
={}&
\frac{\mathbb E f_q(z_L)-\mathbb E f_q(z_0)}{r^2L}
-\langle vf_q'(z)\rangle_L\\
&+\left\langle(1-c^2)a_q(z)f_q''(z)\right\rangle_L.
\end{aligned}
```

The endpoint term vanishes as $`L\to\infty`$ for every fixed positive $`r,\eta`$. The second term is bounded in magnitude by

```math
\left|\langle vf_q'(z)\rangle_L\right|
\le e_{\mathrm W}(q)\sqrt{\langle v^2\rangle_L}.
```

For the real quadrature the last term in the comparison identity vanishes. Section 5.1 therefore proves the two-sided relative comparison

```math
\limsup_{L\to\infty}
\left|\overline e_0(L)-e_{\mathrm W}(q)\right|
\le e_{\mathrm W}(q)T(r,\eta).
```

For an arbitrary adaptive phase, the last term is nonnegative because $`f_q''\ge0`$. Section 5.2 consequently gives

```math
\liminf_{L\to\infty}\overline e_\theta(L)
\ge e_{\mathrm W}(q)\bigl[1-T_{\mathrm{ad}}(r,\eta)\bigr].
```

This proves the theorem. It also explains why reducing the measured signal quadrature cannot improve the leading error through phase-dependent quantum backaction: the lost diffusion appears as a nonnegative term in the comparison identity, while the remaining fast-coordinate correction is uniformly small.

If the real-quadrature quantum filter is stationary, the same calculation gives

```math
\left|e_{\mathrm H,0}^{\mathrm{stat}}-e_{\mathrm W}(q)\right|
\le e_{\mathrm W}(q)T(r,\eta)
```

for every invariant law. Such laws exist because this fixed-phase filter is Feller on the compact Bloch ball. Their uniqueness is unnecessary. For adaptive policies, the time-average proof already covers controllers for which a stationary joint state is not defined.

## 7. Uniform asymptotic regime

For $`r^2+\eta`$ bounded away from one, the explicit roots satisfy

```math
T(r,\eta),\ T_{\mathrm{ad}}(r,\eta)
=O(r^2+\sqrt\eta).
```

The constants can be chosen uniformly in $`q`$: the expressions on the left depend only on $`r,\eta`$, with $`q=r^2/(2\eta)`$. For example, on $`r^2+\eta\le1/2`$ the denominators stay uniformly positive and $`C\le3\eta`$.

It follows that whenever $`\eta\to0`$ and $`r\to0`$,

```math
\frac{e_{\mathrm H}^{\mathrm{opt}}(r,\eta)}
{e_{\mathrm W}(r^2/(2\eta))}
\longrightarrow1.
```

No condition on the behavior of $`q`$ is needed for this relative comparison. To obtain the logarithmic small-error law, also take $`q\to0`$. Equivalently, let $`\eta\to0`$, $`q\to0`$ and set $`r^2=2\eta q`$. Then

```math
e_{\mathrm H}^{\mathrm{opt}}(r,\eta)
\sim\frac q4\log\frac1q.
```

A sequential limit is also valid: hold $`q>0`$ fixed, send $`r\to0`$ with $`\eta=r^2/(2q)`$, and then send $`q\to0`$.

For equal output sharing, $`\eta=1/R`$ and $`q=R\Omega^2/(8\Gamma^2)`$. The simultaneous regime is therefore

```math
R\to\infty,
\qquad
\frac{R\Omega^2}{\Gamma^2}\to0.
```

The exact qubit source and the optimized diffusive receiver then obey

```math
e_{\mathrm H}^{\mathrm{opt}}
\sim
\frac{R\Omega^2}{32\Gamma^2}
\log\frac{8\Gamma^2}{R\Omega^2}.
```

The order of limits is part of the statement: long-run errors are defined at each fixed set of physical parameters, and the resulting bounds are uniform in the subsequent small-parameter regime. No uniform finite-observation-time equilibration bound is asserted.

The relative estimate is essential here. Since $`e_{\mathrm W}(q)`$ itself tends to zero, an absolute approximation error independent of $`e_{\mathrm W}`$ would not determine the leading tracking law. The convex Poisson solution supplies exactly the gradient scale needed to bound the error uniformly over every predictable quadrature phase.

