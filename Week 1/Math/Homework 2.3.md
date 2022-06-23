## 2.3.1
### 1
$$C = \frac{1}{N} \sum_{i = 1}^N \left(\phi(x_i) - \overline{\phi(x)}\right)\left(\phi(x_i) - \overline{\phi(x)}\right)^T.$$
### 2
Suppose that $v$ is an eigenvector of $C$.  Then
$$\lambda v = Cv = \frac{1}{N}\sum_{i = 1}^N \left(\phi(x_i) - \overline{\phi(x)}\right)\left[\left(\phi(x_i) - \overline{\phi(x)}\right)^Tv\right].$$
Thus, $\lambda v$ is a linear combination of the list
$$\phi(x_1) - \overline{\phi(x)}, \quad \phi(x_2) - \overline{\phi(x)}, \quad\dots,\quad \phi(x_N) - \overline{\phi(x)},$$
which means so is $v$.

### 3
The $j$th component of $\tilde K\alpha$ is
$$(\tilde K \alpha)_j = \sum_{i = 1}^N \alpha_i \left(\phi(x_j) - \overline{\phi(x)}\right)^T \left(\phi(x_i) - \overline{\phi(x)}\right) = \left(\phi(x_j) - \overline{\phi(x)}\right)^Tv.$$
Multiplying by $\tilde K$ on the left again, we get that the $k$th component of $\tilde K^2 \alpha$ is 
$$\sum_{j = 1}^N \alpha_j \left(\phi(x_k) - \overline{\phi(x)}\right)^T \left(\phi(x_j) - \overline{\phi(x)}\right) \left(\phi(x_j) - \overline{\phi(x)}\right)^T v. \qquad\qquad (1)$$
Using the fact that
$$C = \frac{1}{N}\sum_{j = 1}^N \alpha_j \left(\phi(x_j) - \overline{\phi(x)}\right) \left(\phi(x_j) - \overline{\phi(x)}\right)^T,$$
(1) is equal to
$$\sum_{i = 1}^N \alpha_i \left(\phi(x_k) - \overline{\phi(x)}\right)^T NCv.$$
But $Cv = \lambda v$, so this turns into
$$\sum_{i = 1}^N \alpha_i \left(\phi(x_k) - \overline{\phi(x)}\right)^T N\lambda v = N\lambda (\tilde K\alpha)_k.$$
Thus,
$$\tilde K^2\alpha = N\lambda \tilde K \alpha,$$
as desired.

### 4
Suppose that $\alpha$ is a solution to
$$N \lambda \alpha = \tilde K \alpha.$$
Then, since $N\lambda$ is a scalar,
$$N\lambda \tilde K \alpha = \tilde K(N \lambda \alpha) = \tilde K^2 \alpha,$$
as desired.

### 5
First off, $ee^T$ is the $N \times N$ matrix with every entry equal to $1 / N$.

For ease of typing this up, let $\mu = \overline{\phi(x)}$. 
Note that the component of $ee^TK$ in the $i$th row and $j$th column is
$$\frac{1}{N}\sum_{k = 1}^N \langle\phi(x_k), \phi(x_j)\rangle = \left\langle \frac{1}{N}\sum_{k = 1}^N \phi(x_k), \phi(x_j) \right\rangle = \langle \mu, \phi(x_j) \rangle.$$

Note that the component of $Kee^T$ in the $i$th row and $j$th column is
$$\langle \phi(x_j), \mu \rangle.$$

Finally, the component of $ee^TKee^T$ in the $i$th row and $j$th column is
$$\langle \mu, \mu \rangle.$$

Thus, the component in the $i,j$th location of
$$(I - ee^T)K(I - ee^T) = K - ee^T K - Kee^T + ee^TKee^T.$$
equals
$$\langle \phi(x_i), \phi(x_j) \rangle - \langle \phi(x_i), \mu \rangle - \langle \mu, \phi(x_j) \rangle + \langle \mu, \mu\rangle = \left\langle \phi(x_i) - \mu, \phi(x_j) - \mu \right\rangle,$$
which is exactly the $i,j$th entry of $\tilde K_{i, j}$, as desired.

### 6
Note that
$$\langle v, v \rangle = \alpha^T \tilde K \alpha.$$
the factor we want is the square root of this.

### 7
Its position in the normalized space is
$$x = \sum_{v} \frac{\langle x, v \rangle v}{\langle v, v \rangle}$$