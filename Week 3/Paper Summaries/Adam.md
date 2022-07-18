# Adam: A Method for Stochastic Optimization

In "Adam:  A Method for Stochastic Optimization," Kingma & Ba propose a method for stochastic optimization using exponentially decaying weighted averages of the first and second moments of the gradient.  It's quite similar to gradient descent, but works much better for stochastic optimization, in which the evaluation function changes over time.  The weighted averages are calculated as follows:
1. Initialize $m_0 = v_0 = \vec 0$, where $m_t$ is the first moment and $v_t$ is the second moment.
2. Initialize constants $\beta_1, \beta_2 \in [0, 1)$.  The authors recommend $\beta_1 = 0.9$ and $\beta_2 = 0.999$.
3. At time step $t$, let $g_t$ be the gradient.  Update  $$
   \begin{align*}
   m_t &= \beta_1 \cdot m_{t - 1} + (1 - \beta_1) \cdot g_t\\
   v_t &= \beta_1 \cdot v_{t - 1} + (1 - \beta_1) \cdot g_t^2\\
   \end{align*}$$
4. These estimates are biased downwards because of the initializations to $0$, so fix them by dividing by $1 - \beta_1^t$ or $1 - \beta_2^t$.
5. Take a step in the negative $\hat m_t / \sqrt{\hat v_t}$ direction, where $\hat m_t$ and $\hat v_t$ are the unbiased estimates of the first and second moments.

Adam is comparable to other top stochastic optimizers like SGD and AdaBoost.  It is guaranteed to find the local minimum for convex online learning problems.