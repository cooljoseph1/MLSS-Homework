## 3.1.1
### 1
First off, $\rho_\tau(z)$ is a convex function, since
$$\rho_\tau(z) = \max(z\tau, z(\tau - 1))$$
can be written as the maximum of two convex functions.  Similarly,
$$f(w) = \sum_{i} \rho_t(y_i - w)$$
is convex, being the sum of convex functions.  This means that any local minimum of $f$ is also a global minimum.  Now, note that
$$\rho_\tau' = \begin{cases}
\tau - 1 &\text{if }z < 0\\
\tau &\text{otherwise}.
\end{cases}$$
Notice that at $w = y_\tau$,
$$\begin{align*}
f'(y_\tau) &= \sum_i \rho_\tau'(y_i - w)\\
&= \left(\sum_{y_i < w} \rho_\tau'(y_i - w)\right) + \left(\sum_{y_i \ge w} \rho_\tau'(y_i - w)\right)\\
&= N\tau(\tau - 1) + N(1 - \tau)\tau\\
&= 0,
\end{align*}$$
where $N$ is the number of data points.  Thus, $y_\tau$ is a local minimum of $f$, and hence a global minimum as well.  So,
$$\mathrm{argmin}_w\sum_{i} \rho_t(y_i - w) = y_\tau.$$
### 2
It's half the L-1 loss.  It's also half the absolute value.

### 3
Setting
$$u_i = \max(0, y_i - x_i^T\beta)\quad \text{and}\quad v_i = \max(0, x_i^T\beta - y_i)$$
shows that the minimum of
$$f(u, v) = u^T1\tau + v^T1(1 - \tau)$$
subject to
$$X^T\beta - y + u - v = 0$$
is no greater than the minimum of $\sum_{i = 1}^N \rho_\tau(y_i - x_i^T\beta)$.  The other direction follows from the fact that the only way to diminish $f(u, v)$ is to decrease the value of either $u_i$ or $v_i$ in some coordinate $i$.  However, any decrease in $u_i$ must result in an identical decrease in $v_i$, but at least one of these is already $0$, so they can't be decreased any further.  

### 4
The problem is equivalent to minimizing
$$\begin{align*}
L(\beta, u, v, \lambda, \mu, \nu) = \max_{\lambda, \mu, \nu} \min_{\beta, u, v} &\quad u^T1\tau + v^T1(1 - \tau)\\
&- \lambda^T(X^T\beta - y + u - v)\\
&- \mu ^T u - \nu^Tv
\end{align*}$$
subject to $\mu, \nu \ge 0$.

Taking a derivative with respect to $\beta$ tells us this occurs when $X\lambda = 0$.  I.e., $\lambda$ is in the null-space of $X$.  Plugging this in yields that, equivalently, we want to find a saddle point of
$$L_2(u, v, \mu, \nu) = u^T1\tau + v^T1(1 - \tau) - \lambda^T(- y + u - v) - \mu ^T u - \nu^Tv.$$
Taking derivatives with respect to $u$ and $v$ and setting them equal to 0 shows that a saddle point occurs when
$$\mu = 1\tau - \lambda \quad\text{and}\quad \nu = 1(1 - \tau) + \lambda.$$
The constraints $\mu \ge 0$ and $\nu \ge 0$ require that
$$\lambda \leq 1\tau \quad\text{and}\quad \lambda \ge 1(\tau - 1).$$
Plugging this in gives the equivalent maximization of
$$L_3(\lambda) = \lambda^T y$$
subject to $\tau - 1 \leq \lambda_i \leq \tau$ for all $i$, and $\lambda$ is in the null-space of $X$.  Setting
$$z = \lambda + 1(1 - \tau)$$
gives the formulation
$$\max_{z} z^T y, \quad\text{subject to}\quad Xz = (1 - \tau)X1, z \in [0, 1]^N,$$
as desired.

### 5
Using complementary slackness,
$$\lambda_i(y_i - x_i^T \beta - u_i + v_i) = 0$$
for all $i$.  Since $\mu_i = \tau - \lambda_i$ and $\nu_i = 1 - \tau + \lambda_i$, this can be simplified to
$$\lambda_i(y_i - x_i^T\beta + 1 - 2\tau + 2\lambda_i) = 0.$$
Replacing $\lambda_i = z_i + \tau - 1$ gives
$$(z_i + \tau - 1)(y_i - x_i^{T}\beta + 2z_i - 1) = 0.$$
Thus, if $z_i = 0$,
$$y_i - x_i^T\beta - 1 = 0 \Longrightarrow y_i - x_i^T\beta = 1.$$
If $z_i = 1$, then $y_i - x_i^T\beta = -1$.
If $z_i \in (0, 1)$, then there are two cases to consider:
- If $z_i = 1 - \tau$, then $y_i - x_i^T\beta$ can be anything.
- Otherwise, $y_i - x_i^T\beta = 1 - 2z_i$.

### 6
```
tau = 0.75 | slope = 0.21740773372818534 | intercept = 0.4492025040398797
tau = 0.5 | slope = 0.23820824709390254 | intercept = -0.3307244016150209
tau = 0.25 | slope = 0.22136016726775787 | intercept = -0.9926835520240038
```
Look at the code for more details.