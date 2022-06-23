## 2.4.1
### 1
The minimum occurs at $\lambda = 0$, $\lambda = +\infty$, or when
$$\frac{d}{d\lambda} \left(\lambda + \frac{x^2}{\lambda + d}\right) = 1 - \frac{x^2}{(\lambda + d)^2} = 0.$$
The latter occurs only if $|x| \ge d$, when $\lambda = |x| - d$.  Testing out these three values for $\lambda$, the minimum is $x^2 / d$ if $|x| > d$ and $2|x| - d$ otherwise.

### 2
Take a second derivative to get
$$\frac{\partial^2 B(x, d)}{\partial x^2} = \begin{cases}
\frac{2}{d} & \text{if }|x| \le d,\\
0 & \text{if } |x| > d.
\end{cases}$$
This is non-negative everywhere, so $B$ is convex in $x$ (for fixed $d$).

### 3
$$\nabla B = \left\langle \frac{\partial}{\partial x} B, \frac{\partial}{\partial d} B \right\rangle = \begin{cases}
\left\langle \frac{2x}{d}, -\frac{x^2}{d^2} \right\rangle & \text{if } |x| \le d,\\
\left\langle \frac{2x}{|x|}, -1 \right\rangle & \text{if } |x| > d.
\end{cases}$$
### 4
If $d$ is higher, the penalty term $B$ is comparatively less for more extreme values of $x$.

## 2.4.2
### 1
Suppose that there is a strictly feasible solution for which $\|a\|_1 \le 1.$  Then by the triangle inequality
$$|a^Tx| = \left|\sum a_ix_i\right| \le \sum |a_i||x_i| < \sum|a_i| = 1,$$
where the last inequality comes from the fact that $|x_i| < 1$ for all $i$.  This contradicts the fact that $a^Tx = 1$, though.  So, all strictly feasible solutions must have $\|a\|_1 > 1$.
### 2
The Lagrangian is
$$L(x, \mu, \lambda) = \lambda - \sum_{i = 1}^N \left[\frac12d_ix_i^2 + r_ix_i + \frac12\mu_i(x_i^2 - 1) + \lambda a_ix_i\right].$$
We have the constraints $\mu_i \ge 0$ for all $i$ and $\sum a_ix_i = 1$.
We want to minimize this Lagrangian$ for all $i$.  Note that
$$\frac{\partial}{\partial x_i} L(x, \mu, \lambda) = d_ix_i + r_i - \mu_i x_i - \lambda a_i.$$
This is equal to zero at
$$x_i^* = \frac{\lambda a_i + r_i}{d_i + \mu_i}$$
(where the $^*$ is there to remind us that this is where $x_i$ is optimized).  Plugging this into the Lagrangian gives us the dual problem
$$\max_{\mu, \lambda} \lambda - \sum_{i = 1}^N\left[\frac12(d_i - \mu_i)\left(\frac{\lambda  a_i + r_i}{d_i + \mu_i}\right)^2 + \frac{(\lambda  a_i + r_i)^2}{d_i + \mu_i} + \frac12 \mu_i\right]$$
subject to 
