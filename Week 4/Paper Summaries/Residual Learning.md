# Deep Residual Learning for Image Recognition
Neural networks appear to degrade in accuracy (even on the training set) as they get deeper.  However, having deep neural networks is valuable--they are able to implicitly understand higher level features with more layers.  Residual learning is a technique to stop degradation from happening.

The basic building block of residual learning is the following:
![[Residual Learning 2022-07-18 15.24.19.excalidraw.svg]]
An identity function is added to the ReLU.  The identity function creates a shortcut path for gradients to update earlier layers.  Networks with these shortcuts can be much deeper and still efficiently trained.  At the time of its publication, using an ensemble of neural networks with varying depths and residual learning led to the best classification in the world on ImageNet, with a top-5 error of 3.57%.  It was similarly impressive on the CIFAR-10 dataset.

The standard deviation of residual responses indicates that ResNets really do learn residual functions (as opposed to just copying the previous layer through the shortcut), and each residual layer has a smaller impact as more layers are introduced.

ResNets stop improving for extremely large models, but are still trainable.