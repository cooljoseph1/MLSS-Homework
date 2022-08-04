### 1
A 1% improvement at 98% leads to an increase in "Nines of Reliability" of
$$\log_{10}(1 - 98\%) - \log_{10}(1 - 99\%) = \log_{10}(2) \approx 0.301.$$
A 1% improvement at 50% leads to an increase in "Nines of Reliability" of
$$\log_{10}(1 - 50\%) - \log_{10}(1 - 51\%) = \log_{10}(50/49) \approx 0.00877,$$
a vastly smaller amount.  $p = 100\%$ corresponds to a (positive) infinite number of nines of reliability.

A severe limitation of using "Nines of Reliability" is that the statistics isn't as nice as when using ordinary probabilities.  E.g., data in the "Nines of Reliability Format" don't follow the Law of Large Numbers (how do you average $+\infty$ and $0$, which are the only options per data point?) or the Central Limit Theorem.  Instead, everything would have to first be converted back to normal probabilities, synthesized, and then converted back to "Nines of Reliability", which kind of defeats the point of converting all risk measurements into this format.

### 2
It's impossible to "quantify" unknown unknowns.  These unknown unknowns, however, can be very risky.

You don't need to be super precise to understand that some things are risky and need to be accounted for.  E.g., I don't need to know that I will die with probability exactly 98% if I jump out of an airplane to determine that jumping out of an airplane is a risk I should not take.

### 3
