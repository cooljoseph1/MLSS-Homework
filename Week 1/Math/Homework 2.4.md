## 2.4.1
### 1
The minimum occurs at $\lambda = 0$, $\lambda = +\infty$, or when
$$\frac{d}{d\lambda} \left(\lambda + \frac{x^2}{\lambda + d}\right) = 1 - \frac{x^2}{(\lambda + d)^2} = 0.$$
The latter occurs only if $|x| \ge d$, when $\lambda = |x| - d$.  Testing out these three values for $\lambda$, the minimum is $x^2 / d$ if $|x| > d$ and $2|x| - d$ otherwise, with the minimum occurring at $\lambda^* = \max(0, |x| - d)$.

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
We have the constraints $\mu_i \ge 0$ for all $i$.
We want to minimize this Lagrangian for all $i$.  Note that
$$\frac{\partial}{\partial x_i} L(x, \mu, \lambda) = -(d_ix_i + r_i + \mu_i x_i + \lambda a_i).$$
This is equal to zero at
$$x_i^* = -\frac{\lambda a_i + r_i}{\mu_i + d_i}$$
(where the $^*$ is there to remind us that this is where $x_i$ is optimized).  Plugging this into the Lagrangian (and simplifying a lot) gives us the dual problem
$$\min_{\mu, \lambda} \lambda + \frac12\sum_{i = 1}^N\left[\mu_i + \frac{(\lambda  a_i + r_i)^2}{\mu_i + d_i} \right]$$
subject to $\mu_i \ge 0$ for all $i$.

### 3
For the tuple $(x^*, \mu, \lambda)$ to satisfy the KKT conditions, we need the following:
**Stationary:**
For all $i$, 
$$d_ix_i + r_i + \lambda a_i+ \mu_i x_i = 0$$
This is how we defined $x^*_i$ earlier, so this is always satisfied at $x^*$.

**Primal feasibility:**
$$\sum_{i = 1}^N a_ix_i^* = 1.$$
and
$$(x_i^*)^2 \le 1$$
for all $i$.  Equivalently,
$$|\lambda a_i + r_i| \le |\mu_i + d_i|.$$

**Dual feasibility:**
This is the constraint $\mu_i \ge 0$ for all $i$.

**Complementary slackness:**
$$\sum_{i = 1}^N \mu_i ((x_i^*)^2 - 1) = 0.$$

Slater's condition and part 1 tells us this characterizes the optimal solution when $\|a\|_1 > 1$.

### 4
It doesn't matter what order we do the minimization, so the dual problem is the same as
$$\min_{\lambda} \min_{\mu} \lambda + \frac12\sum_{i = 1}^N\left[\mu_i + \frac{(\lambda  a_i + r_i)^2}{\mu_i + d_i} \right] = \min_\lambda \lambda + \frac12 \sum_{i = 1}^N B(r_i + \lambda a_i, d_i),$$
since that's how $B(r_i + \lambda a_i, d_i)$ is defined.  Of course, we then have to make sure our constraints our satisfied.  Since the $\mu_i$ is optimized at
$$\mu_i^* = \max(0, |r_i + \lambda a_i| - d_i),$$
this is what we should plug in to calculate $x_i^*$ and make sure the constraints work.  In fact, this value of $\mu_i^*$ guarantees that $|x_i^*| \le 1$, so we have one fewer constraint to worry about.

### 5
Define $A(\lambda) = 1 - \sum a_i x_i^*$, where $x_i^*$ is the optimal value for $x_i$ for the given lambda.  We want to find
$$\min_\lambda \lambda + \frac12 \sum_{i = 1}^N B(r_i + \lambda a_i, d_i)$$
given that $A(\lambda) = 0$.

There are $2N$ critical points for $\lambda$ for which $x_i^*$ switches from being $\pm 1$ to being in the interval $(-1, 1)$.  Name these critical points $\lambda_1, \lambda_2, \dots, \lambda_{2N}$. $A(\lambda)$ is linear between any pair of these critical points, and constant to the left and right of the extremes.  This means that the following algorithm is guaranteed to find all points for which $A(\lambda) = 0$.

1. Compute the critical points $\lambda_1, \lambda_2, \dots, \lambda_{2N}$.  These occur when $|r_i + \lambda a_i| = d_i$.  This can be done in $O(N)$ time.  While you do so, record which $x_i^*$ each critical point corresponds to.  This allows you to compute the change of the slope of $A(\lambda)$ at each critical point in $O(1)$ time.
2. Compute $A(\lambda_i) = 1 - \sum a_i x_i^*$ at each of the critical points.  This can be done in $O(N)$ time by keeping track of the slope of $A(\lambda)$ between critical points.
3. Loop through the critical points, recording which pairs of consecutive points $(A(\lambda_i), A(\lambda_{i+1}))$  have opposite signs.  This can be done in $O(N)$ time.
4. Between each of these pairs of points, calculate the value of $\lambda$ makes $A(\lambda) = 0$.  This is 

### 6
To recover the primal solution $x$, use the fact that
$$\mu_i = \max(0, |r_i + \lambda a_i| - d_i)$$
to compute
$$x_i = \frac{\lambda a_i + r_i}{\mu_i + d_i}.$$
This can be combined all together to get
$$x_i = \begin{cases}
\frac{\lambda a_i + r_i}{d_i} & \text{if } |r_i + \lambda a_i| \le d_i\\
\frac{\lambda a_i + r_i}{|\lambda a_i + r_i|} & \text{if } |r_i + \lambda a_i| > d_i.
\end{cases}$$