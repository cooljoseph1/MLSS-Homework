## 1.1
### 1
$$P(x \mid p) = \prod_{d=1}^D p_d^x(1 - p_d)^{1 - x}.$$
### 2
$$P(x^{(i)} \mid \mathbf p, \pi) = \sum_{k=1}^K P(x^{(i)} \mid p^{(k)})\pi(k).$$
### 3
The log likelihood is
$$\sum_{i=1}^n \log P(x^{(i)} \mid \mathbf p, \pi).$$
## 1.2
### 1
The probability that $p^{(k)}$ was chosen for $x^{(i)}$ to be drawn from is $\pi(k)$.  So,
$$
\begin{align*}
P(z^{(i)} \mid \pi) &= \sum_{k=1}^K \pi(k) z^{(i)}_k.
\end{align*}
$$
For the second question, the indicator variable tells us that the distribution we are drawing from is
$$p = \sum_{k=1}^K z^{(i)}_k p^{(k)} = \langle z^{(i)}, \mathbf p\rangle.$$
So, the probability $x^{(i)}$ is selected is
$$P\left(x^{(i)} \mid \langle z^{(i)}, \mathbf p\rangle\right)$$
Note that $\pi$ isn't actually a factor.

### 2
By Bayes' law (and assuming independence of the $x^{(i)}$),
$$\begin{align*}
P(X, Z \mid \pi, \mathbf p) &= P(X \mid Z, \pi, \mathbf p)P(Z \mid \pi, \mathbf p)\\
&= P(X \mid Z, \pi, \mathbf p)P(Z \mid \pi)\\
&= \left(\prod_{i=1}^n P(x^{(i)} \mid z^{(i)}, \pi, \mathbf p\right)\left(\prod_{i=1}^n P(z^{(i)} \mid \pi )\right).
\end{align*}$$
### 3
Use the definition of conditional expectation and Bayes' theorem:
$$
\begin{align*}
\ &=\\
a
\end{align*}
$$