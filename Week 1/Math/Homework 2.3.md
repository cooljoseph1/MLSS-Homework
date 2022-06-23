## 2.3.1
### 1
$$C = \frac{1}{N} \sum_{i = 1}^N \left(\phi(x_i) - \overline{\phi(x)}\right)\left(\phi(x_i) - \overline{\phi(x)}\right)^T.$$
### 2
Suppose that $v$ is an eigenvector of $C$.  Then
$$\lambda v = Cv = \sum_{i = 1}^N \left(\phi(x_i) - \overline{\phi(x)}\right)\left[\left(\phi(x_i) - \overline{\phi(x)}\right)^Tv\right].$$
Thus, $\lambda v$ is a linear combination of the list
$$\phi(x_1) - \overline{\phi(x)}, \quad \phi(x_2) - \overline{\phi(x)}, \quad\dots,\quad \phi(x_N) - \overline{\phi(x)},$$
as desired.
### 3
