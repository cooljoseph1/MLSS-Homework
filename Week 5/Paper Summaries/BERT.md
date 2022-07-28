# BERT: Pre-training of Deep Bidirectional Transformers for Language Understanding
Much of the first four papers is the authors' insistence that their paper is unique because they "do not use traditional left-to-right or right-to-left models".  Indeed, they almost appear to try to hide evidence of others' use of bidirectional methods in order to make their work seem more innovative, such as by barely citing Mikolov et al.'s paper about word2vec at all in their "Related Work" section, in stark contrast to their paragraphs and paragraphs of text about other, left-to-right models.

The authors then briefly touch on their what their "innovation" actually is:  Instead of masking all future words, just mask a random fraction of all the words and predict what the values behind the masks are.

The authors then spend a while discussing their experiments with fine-tuning their model.  They do much, much better than the next best model (most often OpenAI GPT) on a wide variety of tasks, and are even superhuman on one.

They conclude by stating, yet again, that their method is so innovative because it is "*bidirectional*" (their emphasis, not mine).

## Weaknesses
- Their work is hardly innovative.
- Their choice of replacing the `[Mask]` token with random tokens 10% of the time is arbitrary, and any gains are in large part due to randomness.  Their chosen model's results in the table in Appendix C.2 all fall within two standard deviations of the other models' results.
- There are basically no new problems that BERT solves.  It just does a better job at solving problems other neural networks have already mostly solved.