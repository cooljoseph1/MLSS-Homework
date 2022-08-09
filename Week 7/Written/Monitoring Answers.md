### 1
a) The calibration error is always $\varepsilon$, so the RMS calibration error is also $\varepsilon$.
b) The calibration error is always $50\%$, so the RMS calibration error is $50\%$.
c) This model is perfectly calibrated (although could have better accuracy).

### 2
a) True.
b) False.  It can increase calibration, though.
c) True.  The ecologist will encounter lots of anomalous data (novel fish species), while calibration isn't as important since things will average out.
d) False.  Totally false.  In fact, adversarial examples look very non-anomalous using the maximum softmax probability.

### 3
a) False.  Why would this be true?
b) False.  AUROC remains unchanged.
c) True.  But this is a rather contrived example.

### 4
a) False.
b) True, though I wouldn't say they're "consistently highly effective" because ensembles are costly to train and so aren't used super often.
c) True.  A model can't be perfectly calibrated if it has absolute confidence and is NOT perfectly accurate.
d) False.  It depends on what you mean by "accurate", though.  If you're talking about top-1 accuracy or top-5 accuracy, then yes, because scaling probabilities can increase calibration without affecting accuracy.  If you're talking about absolute error (i.e. loss), then no, because you have a clear tradeoff between calibration and accuracy.

### 5
I assume by $H(\mathcal U; p)$, you mean 