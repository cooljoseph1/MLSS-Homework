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
$$(\tilde K \alpha)_j = \sum_{i = 1}^N \alpha_i \left(\phi(x_i) - \overline{\phi(x)}\right)^T \left(\phi(x_j) - \overline{\phi(x)}\right).$$
Multiplying by $\tilde K$ on the left again, we get that the $k$th component of $\tilde K^2 \alpha$ is 
$$\sum_{j = 1}^N \sum_{i = 1}^N \alpha_i \alpha_j \left(\phi(x_i) - \overline{\phi(x)}\right)^T \left(\phi(x_j) - \overline{\phi(x)}\right) \left(\phi(x_j) - \overline{\phi(x)}\right)^T \left(\phi(x_k) - \overline{\phi(x)}\right).$$
Rearranging the order of summation, and noting that
$$C = \sum_{j = 1}^N \alpha_j \left(\phi(x_j) - \overline{\phi(x)}\right) \left(\phi(x_j) - \overline{\phi(x)}\right)^T,$$
the above is equal to
$$\sum_{i = 1}^N \alpha_i \left(\phi(x_i) - \overline{\phi(x)}\right)^T C\left(\phi(x_k) - \overline{\phi(x)}\right)$$

Since
$$v = \sum_{j = 1}^N \alpha_j \left(\phi(x_j) - \overline{\phi(x)}\right),$$
the inner product
$$\left \langle \phi(x_i) - \overline{\phi(x)}, v\right \rangle = \sum_{j = 1}^N \alpha_j \left<\phi(x_i) - \overline{\phi(x)}, \phi(x_j) - \overline{\phi(x)}\right>,$$
which equals the $i$th component of $\tilde K \alpha$.  So, letting
$$\Phi = \begin{bmatrix}
\phi(x_1) - \overline{\phi(x)}\\
\phi(x_2) - \overline{\phi(x)}\\
\cdots\\
\phi(x_N) - \overline{\phi(x)}
\end{bmatrix},$$
we get that
$$\Phi v = \tilde{K}\alpha.$$
Thus,
$$\tilde K^2\alpha = \tilde K \Phi v = $$