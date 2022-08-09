# ViM: Out-Of-Distribution with Virtual-logit Matching
Out-of-distribution (OOD) detection is important for a variety of reasons (e.g. detecting when the model is being deployed in situations it shouldn't be).  This paper describes a method to do OOD detection by creating a virtual logit that represents how out of distribution the input is.

They review other methods and point out how they are lacking (e.g. methods using logits/probabilities, features that depend on the nullspace of the weight matrix are not considered).

They next build up to what their Virtual-logit Matching is by reviewing some of the math regarding OOD scores based on the null space and principal space (where "principal space" is defined as a small subspace spanned by the largest eigenvectors of $X^TX$).

Here's how the Virtual-logit Matching works.  First, construct the "principal subspace $P$" by taking the space spanned by the largest $D$ eigenvectors of $X^TX$, (where $X$ are the values taken right before the logits, and $D$ is some constant).  Then, create a virtual logit for the OOD by taking the norm of the component of $x$ orthogonal to $P$, and scaling this norm so that it is approximately equal to the maximum of the original logits.  The probability of being OOD is calculated using softmax, just like the probabilities for the other classes.

ViM is similar to adding energy and some residual information.

The authors also created their own dataset, called OpenImage-O, to benchmark various OOD methods.  Their results significantly outperformed almost all other methods (using the AUROC metric) across a large number of OOD benchmarks, including OpenImage-O, Texture, iNaturalist, and ImageNet-O.  Mahalanobis, though, had similar performance, although it is much more computationally costly.

Hyperparameters can also be tuned.  ViM is fairly robust to changes in dimension ($D$), but figuring out a good value of $\alpha$ can be hard to do.

### Judge
The paper fails to evaluate how ViM performs against adversarial images.  (I.e., images generated specifically to fool it.)  I suspect that ViM would be rather weak against adversarial attacks.