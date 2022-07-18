Layer normalization consists of normalizing each layer in the neural network so that the expected value of the neurons are $0$ and their variance is $1$.  Note that this differs from batch normalization because batch normalization takes the expected value and variance for a *single* neuron over all the training data (or an estimate done by batches) whereas layer normalization takes the expected value and variance over all the neruons in a single layer in a single instance of the training data.

Batch normalization, weight normalization, and layer normalization are all invariant to different modifications of the dataset.  Layer normalization is invariant to weight matrix re-scaling, weight matrix re-centering, dataset re-scaling, and single training case re-scaling.  It is not invariant to weight vector re-scaling and dataset re-centering.

The paper then goes into some Riemannian geometry that doesn't serve much of a purpose except showing off how smart the author is.  (Maybe I'm missing something, but the conclusion they come to, "The curvature along the $w_i$ direction will change by a factor of $\tfrac12$ because the $\sigma_i$ will also be twice as large," could probably have been explained solely using first-year differential equations.)

Empirically, layer normalization is competitive with or better than other methods (e.g. batch normalization & no normalization) on a large number of tasks, including handwriting generation, filling in blanks, and skip-thought generation.  Layer normalization is worse at training convolutional networks, however.

## Weakness
This does very little to stop overfitting.  It also 