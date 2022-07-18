## 3.4
### 1
One Lagrangian function is
$$L(x, \lambda) = f(x) + \sum_{i} \lambda_ig_i(x) + \sum_j \lambda_j f_j(x).$$
### 2
Let
$$S = \{x \mid g(x) \leq 0 \text{ and } f(x) = 0\}.$$
Then
$$\bar L(\lambda) = \inf_x L(x, \lambda) \le \inf_{x \in S} L(x, \lambda) \leq \inf_{x \in S} f(x) = f(x^*).$$
Also,
$$\sup_{\lambda_i \ge 0} \bar L(\lambda) \leq \sup_{\lambda_i \geq 0} f(x^*) = f(x^*).$$

### 3
If $(x^*, \lambda^*)$ is a saddle point, then
$$L(x^*, \lambda) \leq L(x^*, \lambda^*)$$
for all $\lambda \in \mathbb R_{\ge 0}^m \times \mathbb R^k$.  Suppose that $f_j(x^*) \neq 0$ for some $j$.  Then consider the limit as $\lambda_j$ goes to $\pm \infty$ (with the sign chosen such that $\lambda_j f_j(x^*) \to +\infty$), fixing everything else.  This would cause the LHS to go to $+\infty$, which contradicts the fact that $L(x^*, \lambda)$ is bounded above by $L(x^*, \lambda^*)$.

Likewise,
$$\lambda_i^*g_i(x^*) = 0$$
for all $i$, because if $g_i(x^*) > 0,$ then $\lambda_i$ can be chosen so that the LHS goes to $+\infty$.  Thus, $g_i(x^*) \le 0$ for all $i$, which makes $\lambda_i^*g_i(x^*) \leq 0$.  Equality can be achieved by setting $\lambda_i^*$ to $0$, and increasing $\lambda_ig_i(x^*)$ will only increase $L(x^*, \lambda)$, so equality will occur for the optimal value.  Combining this together reveals that
$$L(x^*, \lambda^*) = f(x^*).$$

### 4
Let $x'$ be the optimum of the primal.  Then $f(x') \leq f(x^*)$.  On the other hand, combining part (3) with part (1) reveals that
$$f(x^*) = L(x^*, \lambda^*) = \inf_x L(x, \lambda^*)\le f(x').$$
Thus, $f(x^*) = f(x')$, and so $x^*$ is an optimum of the primal.

### 5
The KKT conditions are
1. Stationary:  The derivative of the Lagrangian with respect ot $x$ is 0.  I.e. $$f'(x) + \sum_{i} \lambda_i^* g_i'(x^*) + \sum_j \lambda_j^* f_i'(x^*) = 0.$$
2. Primal feasibility.  $g_i(x^*) \leq 0$ for all $i$ and $f_j(x^*) = 0$ for all $j$.
3. Dual feasibility:  $\lambda_i^* \ge 0$ for all $i$.
4. Complementary slackness:  $$\sum_{i = 1}^m \lambda_i^* g_i(x^*) = 0.$$
### 6
Assuming primal feasibility, dual feasibility, and complementary slackness, we have
$$L(x^*, \lambda^*) = f(x^*).$$
On the other hand,
$$L(x^*, \lambda) = f(x^*) + \sum_{i} \lambda_ig_i(x^*) + \sum_j \lambda_j f_j(x^*).$$
Since $f_j(x^*) = 0$, this is equal to
$$f(x^*) + \sum_{i} \lambda_ig_i(x^*).$$
Since $g_i(x^*) \leq 0$, this is less than or equal to $f(x^*)$, as desired.

### 7
Since $\lambda_i \ge 0$, $\lambda_i g_i$ is a convex function.  The sum of convex functions and affine functions is again a convex function.  Therefore,
$$\ell(x) \triangleq L(x, \lambda^*)$$
is a convex function.  The stationary condition implies that that $\ell(x^*)$ is the minimum value of $\ell(x)$ (since the derivative of a convex function is only $0$ at the minimum).  This means that $L(x^*, \lambda^*) \leq L(x, \lambda^*)$ for all $x$.