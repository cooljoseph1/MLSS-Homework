## 3.4
### 1
One Lagrangian function is
$$L(x, \lambda) = f(x) + \sum_{i} \lambda_ig_i(x).$$
### 2
Let $S = \{x \mid g_i(x) \leq 0 \text{ for all } i\}$.  Then
$$\bar L(\lambda) = \inf_x L(x, \lambda) \le \inf_{x \in S} L(x, \lambda) \leq \inf_{x \in S} f(x) = f(x^*).$$
Also,
$$\sup_{\lambda \ge 0} L(x, \lambda) = \sup_{\lambda \geq 0} f(x) + \sum_{i} \lambda_ig_i(x) = f(x) + \sup_{\lambda \ge 0} \sum_i \lambda_i g_i(x) \leq f(x),$$
with equality when $\lambda = 0$ (since all of the $g_i$ are non-positive).

### 3
If $(x^*, \lambda^*)$ is a saddle point, then
$$L(x^*, \lambda) \le $$