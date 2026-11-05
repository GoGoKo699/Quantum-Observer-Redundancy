# Calibration, loss, and dark counts

The ideal counting receiver obtains its low error by making one pointer state exactly dark. Calibration errors and dark counts change that mechanism. They can be included in the same block master equation, giving an exact stationary accuracy budget for this receiver.

These results describe the specified policy: displace according to the stored bit and reverse that bit after every registered click. They do not claim that this policy remains optimal when the detector is imperfect, or that its error floor is unavoidable for all receivers.

## 1. A source-preserving imperfect instrument

Write the relative complex displacement as

```math
\beta=a e^{i\phi},\qquad a\ge0,
```

with ideal value $`\beta=1`$. An observer of effective branch strength $`\gamma`$ uses the jump operator

```math
J_g=\sqrt\gamma(Z-g\beta I).
```

Independent dark clicks occur at rate $`d\ge0`$ and reverse the stored bit without acting on the source. The joint block generator is

```math
\dot\rho_g
=\mathcal L\rho_g-J_g\rho_gJ_g^\dagger
+J_{-g}\rho_{-g}J_{-g}^\dagger
+d(\rho_{-g}-\rho_g).
```

Its sum remains $`\dot\rho=\mathcal L\rho`$ for every $`\beta,d`$. Complex displacement must be handled consistently: unlike real displacement,

```math
\mathcal D[J_g]\rho
=\gamma\mathcal D[Z]\rho
+i\gamma g\operatorname{Im}\beta[Z,\rho].
```

Consequently the equivalent no-count representation uses

```math
H_g=\frac{\Omega X}{2}+\gamma g\operatorname{Im}\beta\,Z
```

together with $`(\Gamma-\gamma)\mathcal D[Z]`$ and the anticommutator loss from $`J_g`$. This Hamiltonian term belongs to the representation of the output instrument. It cancels the displacement term in the dissipator; it is not a physical feedback drive applied to the source. The source-preserving block equation avoids confusing those two operations.

## 2. Exact stationary error

Use the correlations $`c_z,c_y`$ defined in [the ideal receiver](counting.md), and set $`x=\operatorname{Tr}[X(\rho_++\rho_-)]`$. Direct substitution gives

```math
\begin{aligned}
\dot c_z&=\Omega c_y-k_zc_z+4\gamma\operatorname{Re}\beta,\\
\dot c_y&=-\Omega c_z-k_yc_y+4\gamma\operatorname{Im}\beta\,x,\\
\dot x&=-2\Gamma x,
\end{aligned}
```

where

```math
k_z=2\gamma(1+|\beta|^2)+2d,
\qquad
k_y=2[\Gamma+\gamma(|\beta|^2-1)+d].
```

Let

```math
A_\beta=\Gamma+\gamma(|\beta|^2-1)+d>0.
```

The forcing proportional to $`x`$ decays, and the remaining stable two-dimensional system gives

```math
c_z^{\mathrm{ss}}
=\frac{4\gamma\operatorname{Re}\beta}
{2\gamma(1+|\beta|^2)+2d+\Omega^2/(2A_\beta)},
\qquad
e_\beta=\frac{1-c_z^{\mathrm{ss}}}{2}.
```

This condition on $`A_\beta`$ is automatic when $`0<\gamma\le\Gamma/2`$. In the full range $`0<\gamma\le\Gamma`$, the only excluded case is $`\gamma=\Gamma,\beta=0,d=0`$. There the undisplaced count rate contains no information about $`Z`$; for $`\Omega>0`$ the bit correlation decays and its limiting error is $`1/2`$.

For an especially useful form, define

```math
B_\beta=1+|\beta|^2,
\qquad C_\beta=|1-\beta|^2,
\qquad
\ell=\frac d\gamma+\frac{\Omega^2}{4\gamma A_\beta}.
```

Since $`B_\beta-C_\beta=2\operatorname{Re}\beta`$,

```math
\boxed{
e_\beta=\frac{C_\beta+\ell}{2(B_\beta+\ell)}.
}
```

For $`0<\epsilon<1/2`$, the exact condition for this receiver to meet the target is therefore

```math
\boxed{
C_\beta+(1-2\epsilon)\ell\le2\epsilon B_\beta.
}
```

This is a finite-parameter condition, without a small-drive expansion. At $`\beta=1,d=0`$, it reduces to the ideal counting criterion.

## 3. What consumes the accuracy budget

At zero drive and with no dark counts, the calibration floor is

```math
e_\beta(\Omega=0,d=0)
=\frac{|1-\beta|^2}{2(1+|\beta|^2)}.
```

Near $`a=1,\phi=0`$,

```math
|1-ae^{i\phi}|^2
=(a-1)^2+a\phi^2+O(\phi^4),
\qquad
e_\beta\sim\frac{(a-1)^2+\phi^2}{4}.
```

With perfect calibration, zero drive and dark-count rate $`d`$, the floor is instead

```math
e_{1}(\Omega=0)=\frac{d}{2(2\gamma+d)}.
```

For joint small errors, $`\beta\to1`$, $`d/\gamma\to0`$, and $`\delta=\Omega^2/(\Gamma\gamma)\to0`$, the exact expression yields

```math
e_\beta
=\frac{|1-\beta|^2}{4}
+\frac d{4\gamma}
+\frac{\Omega^2}{16\Gamma\gamma}
+o\!\left(|1-\beta|^2+\frac d\gamma+\delta\right).
```

The same leading coefficient as the ideal receiver is retained if

```math
|1-\beta|^2=o(\delta),
\qquad
d=o\!\left(\frac{\Omega^2}{\Gamma}\right).
```

Indeed, these conditions imply $`A_\beta/\Gamma\to1`$, $`d/\gamma=o(\delta)`$, and $`e_\beta=(\delta/16)[1+o(1)]`$. If the two imperfections are only of the corresponding order rather than smaller, they preserve an error of order $`\delta`$ with a changed coefficient. A fixed nonzero calibration error eventually prevents this receiver from meeting an arbitrarily small tolerance.

At the ideal many-observer threshold, $`\delta`$ is of order $`\epsilon`$. Preserving the ideal coefficient therefore requires amplitude and phase errors smaller than order $`\sqrt\epsilon`$, and dark-count rate smaller than order $`\Omega^2/\Gamma`$. The logarithmic ideal comparison is not a promise of an unbounded practical gain at fixed detector noise.

## 4. Inefficient detection and output sharing

If an observer receives a physical branch $`\gamma_{\mathrm{raw}}`$ and only a fraction $`\xi\in(0,1]`$ reaches an otherwise ideal detector, use

```math
\gamma=\xi\gamma_{\mathrm{raw}}.
```

The missing part is inaccessible output, so $`\Gamma`$ remains the total source dephasing strength. The displacement is calibrated to the detected amplitude. For $`R`$ equal physical branches, substitute $`\gamma=\xi\Gamma/R`$ into the exact error above.

With perfect calibration and no dark counts this gives the attainable count

```math
R_{\mathrm{null},\xi}
=\left\lfloor
\frac{16\xi\Gamma^2}{\Omega^2}
\frac\epsilon{1-2\epsilon}
\right\rfloor.
```

With general $`\beta,d`$, use the boxed accuracy inequality, including the $`R`$ dependence of $`A_\beta`$. It is preferable to a small-error formula when the calibration floor uses a substantial fraction of the target tolerance.

The present instrument model has no dead time and changes its displacement immediately after a click. Finite response time and phase noise with temporal correlations would require a larger detector model. They are outside the exact formula's assumptions.

## 5. Verification

[The tracking verification script](../verification/verify_tracking.py) compares the formula with independently assembled augmented-generator stationary states for real and complex displacement. Random positive joint states test both the transient correlation equations and the identity that forgetting the record preserves $`\mathcal L`$. These checks include the imaginary-displacement forcing term, which would be lost by incorrectly using the real-displacement no-count generator.
