# Deep Residual Learning for Image Recognition
Neural networks appear to degrade in accuracy (even on the training set) as they get deeper.  However, having deep neural networks is valuable--they are able to implicitly understand higher level features with more layers.  Residual learning is a technique to stop degradation from happening.

The basic building block of residual learning is the following:
![[Residual Learning 2022-07-18 15.24.19.excalidraw]]
An identity function is added to the ReLU.  The identity function creates a shortcut path for gradients to update earlier layers.