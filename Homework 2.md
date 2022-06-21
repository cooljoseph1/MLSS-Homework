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

The probability that $p^{(k)}$ was chosen for $x^{(i)}$ to be drawn from is $\pi(k)$.
$$
\begin{align*}
P(z^{(i)} \mid \pi) &= P(z^{(i)} \mid \mathbf p, \pi
\end{align*}
$$

$$
\begin{align*}
P(z^{(i)} \mid \pi) &= P\left(z^{(i)}\mid x^{(i)} \in \mathrm{Bernoulli}(p^{(k)})\right)P\left(x^{(i)} \in \mathrm{Bernoulli}(p^{(k)})\mid \pi\right)\\
&+ P\left(z^{(i)}\mid x^{(i)} \not \in \mathrm{Bernoulli}(p^{(k)})\right)P\left(x^{(i)} \not \in \mathrm{Bernoulli}(p^{(k)})\mid \pi\right)\\
&= z_i P(x^{(i)}
\end{align*}
$$