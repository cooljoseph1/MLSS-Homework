# The Mythos of Model Interpretability
Interpretability seems to be a loose conglomeration of ideals.  Fundamentally, humans want to understand why models give the decisions they do, and that is what they are looking for when they say a model is "interpretable".  Some kinds of interpretability are *transparancy*, which focuses on understanding the components of a model (i.e. making it less of a black box), and *post hoc interpretations*, which focus on explaining a decision after it has been made (but not revealing the inner working of the model--this is similar to how brains are black boxes but we can still get explanations from humans).

There are many goals of interpretability.  One of the biggest is being able to trust models.  If we can understand them, we are better able to know when they might fail.  Being interpretable can also help us see where causal relationships might make models fail, and where they would be able to transfer well to other datasets.  Interpretability is further useful in providing information beyond a simple number.

What does an interpretable model look like?
- Simulatable -- A human could reasonably run through the calculations needed.  Basically only sparse linear models and short decision trees are interpretable under this criterion.
- Decomposable -- The model can be broken down into intuitive/understandable parts.