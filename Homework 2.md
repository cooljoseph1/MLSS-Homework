## 1.1
### 1
$$P(x \mid p) = \prod_{d=1}^D p_d^{x_d}(1 - p_d)^{1 - x_d}.$$
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
Note that $\pi$ isn't actually a factor.  Also:  This can be written another way as
$$\prod_{k = 1}^K\left(\prod_{d=1}^D p_d^{x^{(i)}_d}(1 - p_d)^{1 - x^{(i)}_d}\right)^{z_k}.$$

### 2
By Bayes' law (and assuming independence of the $x^{(i)}$),
$$\begin{align*}
P(X, Z \mid \pi, \mathbf p) &= P(X \mid Z, \pi, \mathbf p)P(Z \mid \pi, \mathbf p)\\
&= P(X \mid Z, \pi, \mathbf p)P(Z \mid \pi)\\
&= \left(\prod_{i=1}^n P(x^{(i)} \mid z^{(i)}, \pi, \mathbf p)\right)\left(\prod_{i=1}^n P(z^{(i)} \mid \pi )\right).
\end{align*}$$
### 3
Since $z^{(i)}$ is an indicator variable,
$$
\begin{align*}
\eta\left(z^{(i)}_k\right) &= E\left[z_k^{(i)} \mid x^{(i)}, \pi, \mathbf p\right] = P\left(z_k^{(i)} = 1 \mid x^{(i)}, \pi, \mathbf p\right).
\end{align*}
$$
By Bayes' theorem,
$$
\begin{align*}
P\left(z_k^{(i)} = 1 \mid x^{(i)}, \pi, \mathbf p\right) &= \frac{P\left(x^{(i)} \mid z_k^{(i)} = 1, \pi, \mathbf p\right) P(z_k^{(i)} = 1 \mid \pi, \mathbf p)}{P\left(x^{(i)} \mid \pi, \mathbf p\right)}\\
&= \frac{P\left(x^{(i)} \mid p^{(k)}\right)\pi_k}{P\left(x^{(i)} \mid \pi, \mathbf p\right)}
\end{align*}.
$$
All of these are answers we already have.  Plugging those in, we get
$$\eta\left(z^{(i)}_k\right) = \frac{
	\pi_k \prod_{d=1}^D
	\left(p^{(k)}_d\right)^{x^{(i)}_d}
	\left(1 - p^{(k)}_d\right)^{1 - x^{(i)}_d}
}{\sum_{j=1}^n
	\pi_j \prod_{d=1}^D
	\left(p^{(j)}_d\right)^{x^{(i)}_d}
	\left(1 - p^{(j)}_d\right)^{1 - x^{(i)}_d}
},$$
as desired.

For the second part, let $A_k$ be the event that $p = p^{(k)}$.
$$\begin{align*}
\log P(X, Z \mid \pi, \mathbf p) &= \left(\prod_{i=1}^n P(x^{(i)} \mid z^{(i)}, \pi, \mathbf p)\right)\left(\prod_{i=1}^n P(z^{(i)} \mid \pi )\right).\\
&= \sum_{i = 1}^n \log P(x^{(i)} \mid z^{(i)}, \pi, \mathbf p) + \log P(z^{(i)} \mid \pi)\\
&= \sum_{i=1}^n \left(\sum_{k = 1}^K\right)
\end{align*}$$