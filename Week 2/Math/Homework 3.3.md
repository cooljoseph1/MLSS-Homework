## 3.3
### 1
This doesn't make sense...  If $f \in \mathcal{F}(\mathcal{X})$ then $2f$ and $-f$ are also in $\mathcal{F}(\mathcal X)$.  So, the supremum doesn't exist.  Did you intend to define $\mathcal{F}(\mathcal X)$ as a bounded space of continuous functions from $\mathcal X$ to $\mathbb R$, not a space of bounded functions?

The empircal version of this statement would be
$$\sup_{f \in \mathcal F} \left( \frac{1}{m}\sum_{i = 1}^m f(x_i) - \frac1m\sum_{i=1}^m f(y_i) \right).$$
### 2
Your definition of $\phi$ is wrong.  It should be a map from $\mathcal X$ to $\mathcal F$, not to $\mathbb R$.

Replacing $f(x)$ with $\langle f, \phi(x) \rangle_{\mathcal H}$ yields
$$\mathrm{MMD}^2[\mathcal F, p, q] = \left(\sup_{f \in \mathcal F}\ \left\langle f, \mathbb E[\phi(x)] - \mathbb E[\phi(y)]\right\rangle\right)^2.$$
By the Cauchy-Schwartz inequality, this is less than or equal to
$$\|f\|^2\|\mathbb E[\phi(x)] - \mathbb E[\phi(y)]\|^2 \leq \boxed{\Big\|\mathbb E[\phi(x)] - \mathbb E[\phi(y)]\Big\|^2}.$$
### 3
$$\left\|\frac{1}{m}\sum_{i = 1}^m \phi(x_i) - \frac{1}{m}\sum_{i = 1}^m \phi(y_i)\right\|^2$$
### 4
