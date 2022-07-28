# Attention Is All You Need
Earlier methods of using attention combines attention with recurrent neural networks (RNNs), which bottlenecks parallelization (since every timestep requires the previous).  This paper, titled "Attention Is All You Need", proposes to speed up training by only using attention (which is massively parallelizable).

## The Transformer
The transformer is their basic building block.  It consists of an attention block combined with a fully connected feed-forward block, with residual connections in between them.  In this paper, the attention block is multi-headed, meaning that they have many copies of identical looking attention blocks that are concatenated together right before the feed-forward block.

## Masking
It's important to mask future outputs in the decoder so the model actually has to learn to predict the future.  In this paper, that's done by setting to $-\infty$ all those values right before the softmax, effectively zeroing their contribution.

## Feed-forward Networks
The feed-forward networks are fully connected *per position*.  They do not transfer information between different positions (i.e. words).  This is important in the decoder so that early words can't glimpse the future.