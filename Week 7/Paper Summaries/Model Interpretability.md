# The Mythos of Model Interpretability
Interpretability seems to be a loose conglomeration of ideals.  Fundamentally, humans want to understand why models give the decisions they do, and that is what they are looking for when they say a model is "interpretable".  Some kinds of interpretability are *transparancy*, which focuses on understanding the components of a model (i.e. making it less of a black box), and *post hoc interpretations*, which focus on explaining a decision after it has been made (but not revealing the inner working of the model--this is similar to how brains are black boxes but we can still get explanations from humans).

There are many goals of interpretability.  One of the biggest is being able to trust models.  If we can understand them, we are better able to know when they might fail.  Being interpretable can also help us see where causal relationships might make models fail, and where they would be able to transfer well to other datasets.  Interpretability is further useful in providing information beyond a simple number.

What does an interpretable model look like?
- Simulatable -- A human could reasonably run through the calculations needed.  Basically only sparse linear models and short decision trees are interpretable under this criterion.
- Decomposable -- The model can be broken down into intuitive/understandable parts.
- Algorithmic transparency -- The model's algorithm can be proven to have certain properties such as convergence or nice decision boundaries.
What are some post-hoc methods?
- Text explanation -- The model gives a written explanation of why it made its choices.
- Visualization -- Use something like t-SNE to visualize high dimensional embeddings.  You can also look at what inputs cause certain nodes in a neural network to be highly activated.
- Local explanations -- E.g., saliency maps
- Explain by example -- Give an example of what the model thinks is the closest image to the given one, along with a class prediction.

Linear models are not always more interpretable than deep neural networks.  Although the algorithm is simpler, they don't have the same kind of clear features that the nodes of neural networks have.  Also, transparency might not be what we need; humanity could be better off with less transparent models that are much more accurate or robust.  Finally, be wary of post-hoc interpretations.  They often look really cool, but aren't actually as meaningful as they look.
