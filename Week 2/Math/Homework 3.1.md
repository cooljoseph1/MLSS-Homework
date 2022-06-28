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
Like above, the function to be minimized is convex, so any local minimum is a global minimum.  Split the sum into the cases $y_i < x_i^{T}\beta$ and $y_i \ge x_i^T\beta$ and take a derivative to  get

$$\left(\sum_{y_i < x_i^T \beta}(\tau - 1) \right) + \left(\sum_{y_i \geq x_i^T \beta}\tau \right) = 0.$$

### 4
### 5
### 6
