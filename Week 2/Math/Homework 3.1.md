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
L(\beta, u, v, \lambda, \mu, \nu) &= u^T1\tau + v^T1(1 - \tau) + \lambda^T(X^T\beta - y + u - v)\\
&\qquad \qquad- \mu ^T u - \nu^Tv
\end{align*}$$
subject to $\mu, \nu \ge 0$.
Taking derivatives with respect to $u$ and $v$ gives
$$\mu = 1\tau + \lambda \quad\text{and}\quad \nu = 1(1 - \tau) + \lambda.$$
Plugging this in gives the equivalent minimization of
$$\lambda^T(X^T \beta - y)$$
subject to $\lambda \ge 1\max(-\tau, \tau - 1)$.


### 5
### 6
