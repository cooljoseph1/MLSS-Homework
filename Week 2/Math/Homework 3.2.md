## 3.2.1
### 1
By Bayes' theorem,
$$P(y^* \mid X^*, X, y) = \frac{P(y^*, y \mid X^*, X)}{P(y \mid X^*, X)}.$$
The numerator and denominator on the right are
$$\frac{\exp(-\frac12
\begin{bmatrix}
y\\ y^*
\end{bmatrix}\ 
k([X \quad X^*], [X \quad X^*])^{-1}\  \begin{bmatrix}
y^T & (y^*)^T
\end{bmatrix}}{\sqrt{(2\pi)^{n + m} \ \left|k([X \quad X^*], [X \quad X^*])\right|}}$$
and
$$\frac{\exp(-\frac12y^T\ k(X, X)^{-1}\ y)}{\sqrt{(2\pi)^{n} \  |k(X, X)|}},$$
respectively.  Dividing them gives a new normal distribution.  Using the block matrix inverse for $k([X \quad X^*], [X \quad X^*])^{-1}$ lets us calculate that the mean and covariance matrix of this new normal distribution are
$$k(X^*, X)k(X, X)^{-1}y$$
and
$$k(X^*, X^*) - k(X^*, X)k(X, X)^{-1}k(X, X^*),$$
respectively.