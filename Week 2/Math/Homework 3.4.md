## 3.4
### 1
One Lagrangian function is
$$L(x, \lambda) = f(x) + \sum_{i} \lambda_ig_i(x) + \sum_j \lambda_j f_j(x).$$
### 2
Let
$$S = \{x \mid g(x) \leq 0 \text{ and } f(x) = 0\}.$$
Then
$$\bar L(\lambda) = \inf_x L(x, \lambda) \le \inf_{x \in S} L(x, \lambda) \leq \inf_{x \in S} f(x) = f(x^*).$$
Equality occurs when $x \in 
Also,
$$\begin{align*}
\sup_{\lambda_i \ge 0} L(x, \lambda) &= \sup_{\lambda_i \geq 0} f(x) + \sum_{i} \lambda_ig_i(x) + \sum_j \lambda_j f_j(x)\\
&= f(x) + \sup_{\lambda_i \ge 0} \sum_i \lambda_i g_i(x) + \sum_j \lambda_j f_j(x)\\
&\leq f(x),
\end{align*}$$
with equality when $\lambda_i = 0$ for all $i$ (since all of the $g_i$ are non-positive).

### 3
If $(x^*, \lambda^*)$ is a saddle point, then
$$L(x^*, \lambda) \leq L(x^*, \lambda^*)$$
for all $\lambda \in \mathbb R_{\ge 0}^m \times \mathbb R^k$.  Suppose that $f_j(x^*) \neq 0$ for some $j$.  Then consider the limit as $\lambda_j$ goes to $\pm \infty$ (with the sign chosen such that $\lambda_j f_j(x^*) \to +\infty$), fixing everything else.  This would cause the LHS to go to $+\infty$, which contradicts the fact that $L(x^*, \lambda)$ is bounded above by $L(x^*, \lambda^*)$.

Likewise,
$$\lambda_i^*g_i(x^*) = 0$$
for all $i$, because if $g_i(x^*)$

### 4
THIS IS FALSE.  Consider, for example, the system
$$\min\ x \qquad\text{given } -x \leq 0.$$
with the Lagrangian $L(x, \lambda) = x - \lambda x$.  Then $(x^*, \lambda^*) = (1, 1)$ satisfies the 
right half of the saddle point condition, but $x^*$ is not the optimum solution to the primal.

It's only by using the knowledge of the LHS of the equation that allows this to work
Let $x'$ be an optimum solution to the primal.  Part (2) implies that
$$L(x^*, \lambda^*) = \inf_x L(x, \lambda^*)\le f(x').$$

$$$$