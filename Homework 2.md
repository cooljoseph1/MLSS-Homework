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
$$P(z^{(i)} \mid \pi) = \prod_{d = 1}^D \prod_{k=1}^K \pi(k)^{z^{(i)}_{k}}$$