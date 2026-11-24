# Simultaneous accuracy of displaced-counting observers

The [one-bit displaced-counting receiver](counting.md) has an exact marginal error. When several receivers run on separate branches, their errors are dependent. This page determines their joint stationary law and the allocation that maximizes the probability that every receiver is correct.

Use the [driven-dephasing model](model.md) with total coupling $`\Gamma>0`$, drive $`\Omega>0`$, and fixed branch strengths $`\gamma_i>0`$ for $`i=1,\ldots,R`$. The observed strength satisfies $`\sum_i\gamma_i\le\Gamma`$. Each observer implements ideal one-bit nulling locally and reports its bit $`g_i`$ at the same terminal test. The error event is that at least one reported bit differs from the source measurement $`Z^{\rm test}`$. Stationarity refers to the limit of this single-test experiment as the test time tends to infinity.

## 1. An exact stationary law for arbitrary splitting

Let $`\boldsymbol g`$ be the vector of receiver bits and $`\rho_{\boldsymbol g}`$ the unnormalized source state in that bit sector. Write $`\boldsymbol g^{(i)}`$ for the vector obtained by flipping bit $`i`$. At fixed old bit $`g_i`$, observer $`i`$ has jump $`J_{i,g_i}=\sqrt{\gamma_i}(Z-g_iI)`$. The joint block equation is

```math
\begin{aligned}
\dot\rho_{\boldsymbol g}
&=\mathcal L\rho_{\boldsymbol g}
-\sum_i J_{i,g_i}\rho_{\boldsymbol g}J_{i,g_i}^\dagger
+\sum_i J_{i,-g_i}\rho_{\boldsymbol g^{(i)}}J_{i,-g_i}^\dagger,\\
\mathcal L\rho&=-i[\Omega X/2,\rho]+\Gamma\mathcal D[Z]\rho.
\end{aligned}
```

The two jump sums cancel after summation over the bit sectors. The unconditional source generator retains the full strength $`\Gamma`$, including unreceived output.

Set $`a_i=4\gamma_i`$ and $`\lambda=\Omega^2/(4\Gamma)`$. For a subset $`S`$ of observers, put $`g_S=\prod_{i\in S}g_i`$ and $`a_S=\sum_{i\in S}a_i`$. Define the terminal agreement signs $`b_i=g_i Z^{\rm test}`$. Their moments and the odd-set coherences are

```math
\begin{aligned}
A_S(t)&=\mathbb E\!\left[\prod_{i\in S} b_i\right]
=\sum_{\boldsymbol g}g_S\mathrm{Tr}\bigl(Z^{|S|}\rho_{\boldsymbol g}\bigr),\\
C_S(t)&=\sum_{\boldsymbol g}g_S\mathrm{Tr}(Y\rho_{\boldsymbol g})\quad (|S|\text{ odd}).
\end{aligned}
```

Clicks outside $`S`$ leave $`g_S`$ unchanged. A click inside $`S`$ changes its sign. The identities

```math
J_{i,g_i}^\dagger J_{i,g_i}=2\gamma_i(I-g_iZ),\qquad
J_{i,g_i}^\dagger ZJ_{i,g_i}=2\gamma_i(Z-g_iI),\qquad
J_{i,g_i}^\dagger YJ_{i,g_i}=0
```

give the click contribution $`a_i(A_{S\setminus\{i\}}-A_S)`$ to $`\dot A_S`$ for each $`i\in S`$. The Hamiltonian and dephasing then give

```math
\begin{aligned}
\dot A_S&=\sum_{i\in S}a_i A_{S\setminus\{i\}}-a_S A_S && (|S|\text{ even}),\\
\dot A_S&=\sum_{i\in S}a_i A_{S\setminus\{i\}}-a_S A_S+\Omega C_S && (|S|\text{ odd}),\\
\dot C_S&=-\Omega A_S-2\Gamma C_S && (|S|\text{ odd}).
\end{aligned}
```

$`A_\varnothing=1`$. The homogeneous even-set equation decays at rate $`a_S`$ for every nonempty $`S`$. The odd-set two-dimensional system has negative trace $`-(a_S+2\Gamma)`$ and positive determinant $`2\Gamma a_S+\Omega^2`$. Induction over $`|S|`$ therefore gives convergence from any initial bit and source state. Eliminating $`C_S`$ at stationarity yields

```math
\boxed{
A_S=\frac{\sum_{i\in S}a_i A_{S\setminus\{i\}}}
{a_S+2\lambda\,\mathbf 1_{\{|S|\text{ odd}\}}}.
}
```

The moments determine the stationary distribution of the signs. For $`\boldsymbol c\in\{\pm1\}^R`$ its probability is $`2^{-R}\sum_S A_S\prod_{i\in S}c_i`$.

## 2. Probability that everyone is correct

A classical process gives another way to compute the stationary distribution. A Poisson clock of rate $`\lambda`$ flips every agreement sign together, and independent Poisson clocks of rates $`a_i`$ reset the corresponding signs to $`+1`$. Its stationary moments satisfy the same recursion. The equality applies to the distribution at one terminal test of the quantum experiment.

In this classical representation, let $`T_i`$ be the time since the most recent reset at observer $`i`$. These ages are independent exponentials of rates $`a_i`$, independent of the common flip clock. Every sign is positive precisely when the number of flips is even in each interval between consecutive ordered ages, starting at age zero. On an interval of length $`d`$, the even-parity probability is $`(1+e^{-2\lambda d})/2`$.

For a set $`S`$, the first age has exponential rate $`a_S`$, and observer $`i`$ has that age with probability $`a_i/a_S`$, independently of the first age. The residual ages are independent exponentials by memorylessness. With $`f(x)=(x+\lambda)/(x+2\lambda)`$, averaging the first interval's even-parity probability gives $`f(a_S)`$. The stationary probability $`P(S)`$ that all signs in $`S`$ are positive obeys

```math
P(\varnothing)=1,
\qquad
\boxed{P(S)=f(a_S)\sum_{i\in S}\frac{a_i}{a_S}P(S\setminus\{i\}).}
```

The parameter $`\lambda`$ is held fixed throughout this recurrence. Removing an observer from the event leaves the source's total dephasing rate unchanged.

## 3. Equal splitting is exactly optimal for these receivers

For a set of $`k`$ observers with total rate $`s=\sum_i a_i`$, the success probability at equal rates is

```math
F_k(s)=\prod_{j=1}^k f(js/k).
```

We show $`P(S)\le F_k(s)`$ by induction, with equality for positive rates only at equal splitting. The result is immediate for $`k=1`$. Suppose it holds for $`k-1`$ and write $`F=F_{k-1}`$. The recurrence gives

```math
P(S)\le \frac{f(s)}{s}\sum_{i\in S}G(a_i),
\qquad G(r)=rF(s-r).
```

Each factor of $`F`$ has an increasing, strictly concave logarithm. Indeed,

```math
(\log f)'(y)=\frac{\lambda}{(y+\lambda)(y+2\lambda)},
\qquad 0< y(\log f)'(y)<1\quad(y>0).
```

Consequently $`F'>0`$, $`F''\le (F')^2/F`$, and $`xF'(x)/F(x)<k-1`$. At $`r_0=s/k`$, the last inequality gives $`G'(r_0)>0`$, since $`s-r_0=(k-1)r_0`$. The logarithm of $`G`$ is strictly concave on $`(0,s)`$, so the region where $`G'\ge0`$ is an initial interval containing $`r_0`$. In that interval $`rF'(s-r)/F(s-r)\le1`$ and

```math
G''(r)=rF''(s-r)-2F'(s-r)\le -F'(s-r)<0.
```

The tangent to $`G`$ at $`r_0`$ thus strictly dominates $`G`$ at every other point of the increasing interval. It continues to dominate wherever $`G`$ decreases, because the tangent has positive slope. Summing the tangent bounds at $`a_i`$ and using $`\sum_i(a_i-r_0)=0`$ yields

```math
P(S)\le\frac{f(s)}{s}kG(r_0)
=f(s)F_{k-1}\bigl((k-1)s/k\bigr)=F_k(s),
```

strictly if any $`a_i\ne r_0`$. Since $`F_k(s)`$ is strictly increasing in $`s`$, the best fixed allocation with the budget $`\sum_i\gamma_i\le\Gamma`$ uses every available branch fraction and sets $`\gamma_i=\Gamma/R`$.

## 4. Distribution of the number of errors at equal splitting

With all branches of strength $`\gamma`$, write $`q=\Omega^2/(8\Gamma\gamma)=2\lambda/a_i`$. Symmetry gives $`A_S=A_k`$ for $`|S|=k`$. The moment recurrence becomes

```math
A_k=\frac{k}{k+q\,\mathbf 1_{\{k\text{ odd}\}}}A_{k-1}.
```

Let $`U=2X-1`$ with $`X\sim\mathrm{Beta}(1+q/2,q/2)`$. The density of $`U`$ is proportional to $`(1+u)(1-u^2)^{q/2-1}`$ on $`(-1,1)`$. The even moment $`\mathbb E[U^{2m}]`$ is the $`m`$th moment of a $`\mathrm{Beta}(1/2,q/2)`$ variable, by symmetry and the substitution $`v=u^2`$. The odd moment $`\mathbb E[U^{2m-1}]`$ equals $`\mathbb E[U^{2m}]`$ for $`m\ge1`$, since only the factor $`u`$ in $`1+u`$ contributes. The ratio between successive even moments is $`(2m-1)/(2m-1+q)`$. These are exactly the moments $`A_k`$.

Conditional on $`X`$, independent binary signs that are positive with probability $`X`$ have moments $`\mathbb E[(2X-1)^k]`$. This mixture therefore has the exact stationary sign law. In particular, the number of errors $`K`$ is beta-binomial with trial count $`R`$ and shape parameters $`q/2,1+q/2`$, in that order. Its probability of zero errors is

```math
\boxed{\Pr(K=0)=\prod_{j=1}^R\frac{j+q/2}{j+q}.}
```

At $`R=1`$ this gives error $`q/[2(1+q)]`$, the known marginal law. For arbitrary $`R`$, the beta mixture quantifies the dependence between observer errors.

## 5. The growing-observer limit

Put $`H_R=\sum_{j=1}^Rj^{-1}`$. The logarithm of the exact success probability obeys

```math
0\le \frac{q}{2}H_R+\log\Pr(K=0)
\le\frac{3q^2}{8}\sum_{j=1}^R\frac1{j^2}.
```

Indeed, $`\log[(j+q)/(j+q/2)]=\int_{q/2}^{q}(j+x)^{-1}\,dx`$, and the difference between $`1/j`$ and the integrand is at most $`x/j^2`$. With the full budget equally split, $`q=\Omega^2 R/(8\Gamma^2)`$. Therefore in the joint regime $`\Omega^2 R H_R/\Gamma^2\to0`$,

```math
\Pr(K\ge1)=(1+o(1))\frac{\Omega^2 R H_R}{16\Gamma^2}.
```

The error of a specified observer in the same experiment is asymptotic to $`\Omega^2 R/(16\Gamma^2)`$. The factor $`H_R`$ has a direct interpretation in the classical stationary representation. With equal reset rates, the mean time for every branch to reset is the mean of the maximum of $`R`$ independent exponential waits, namely $`H_R/(4\gamma)`$. At a low common flip rate, this time controls the probability that a recent flip still leaves at least one observer wrong.

For target joint error $`\epsilon\to0`$, let $`B=16\epsilon\Gamma^2/\Omega^2\to\infty`$. The largest feasible number using ideal one-bit nulling with any fixed splitting satisfies

```math
R_{\rm joint}\sim \frac{B}{W(B)},
\qquad W(B)e^{W(B)}=B.
```

To see this, evaluate the joint error at integer counts asymptotic to $`(1\pm\eta)B/W(B)`$ for any fixed $`0<\eta<1`$. There $`R H_R/B\to1\pm\eta`$ and the small-error expansion applies. The exact equal-split success probability decreases with $`R`$, since the added factor is less than one and increasing $`R`$ increases $`q`$ in every earlier factor. The two counts thus bracket the maximum. The [marginal threshold](counting.md#5-equal-sharing-and-verification) for the same receiver is asymptotic to $`B`$ in this regime.

The fixed-split optimum is exact for the ideal one-bit counting policy. Whether another local receiver can improve the simultaneous-correctness scaling is open. The shared-flip representation computes the stationary terminal event. Its rates do not specify a physical trajectory for the driven source.

[Related work](../references/related-work.md#several-observers-and-objectivity) traces the classical beta law and prior consensus criteria. [The independent generator check](../verification/README.md#what-is-checked) verifies the full wrong-guess distribution on small instances.
