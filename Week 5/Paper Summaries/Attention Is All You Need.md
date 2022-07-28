# Attention Is All You Need
Earlier methods of using attention combines attention with recurrent neural networks (RNNs), which bottlenecks parallelization (since every timestep requires the previous).  This paper, titled "Attention Is All You Need", proposes to speed up training by only using attention (which is massively parallelizable).

## The Transformer
The transformer is their basic building block.  It consists of an attention block combined with a fully connected feed-forward block, with residual connections in between them.  In this paper, the attention block is multi-headed, meaning that they have many copies of identical looking attention blocks that are concatenated together right before the feed-forward block.

## Masking
It's important to mask future outputs in the decoder so the model actually has to learn to predict the future.  In this paper, that's done by setting to $-\infty$ all those values right before the softmax, effectively zeroing their contribution.

## Feed-forward Networks
The feed-forward networks are fully connected *per position*.  It's like a 1x1 convolution.  They do not transfer information between different positions (i.e. words).  This is important in the decoder so that early words can't glimpse the future.

## Results
Their results are the next best (though only slightly better at En-Fr) at translating both English to German and English to French.  Their training costs are significantly less on the English-French translation, and about half of the next best model for English-German.

## Judging:
Weakness 1:  It's so inefficient!  In a single attention block, only a small fraction of the values actually matter.  Instead of using a softmax, why can't they just us a max (or k-max)?  This would definitely make backpropagation faster, and probably would also speed up the forward step.

Weakness 2:  Multi-headed attention seems like an unnecessary complication.  See "Single Headed Attention RNN: Stop Thinking With Your Head", for a rather (informal) example of where single headed attention is comparable to multi-headed attention.

Strength:  Attention is useful in tons of applications other than just language processing.  I know, for example, that they've been used in image recognition & captioning.