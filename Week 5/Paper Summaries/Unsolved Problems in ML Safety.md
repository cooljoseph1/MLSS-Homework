# Unsolved Problems in ML Safety
## Robustness
### Black Swans
The unexpected and unusual happen all the time.  How can we make sure ML models don't crash when they encounter such?  This paper proposes data augmentation, having model-environment feedback loops, and having unusual but useful datasets.

### Adverserial Robustness
Right now, most ML systems are super vulnerable to adverserial attacks.  How can we train them to be robust to them?  Some ideas include blackboxing neural networks (making it much harder to train an adversary against them), looking for discrepancies through the use of multiple sensors, and having evolving defenses.

## Monitoring
### Anomaly Detection
Few ML models are designed to detect anomalies.  However, this could be incredibly useful to determine if an adversary is attacking it or to determine if humans should take a closer look at what is going on.  Past research in anomaly detection includes out-of-distribution detection, open-set detection, and one-class learning.  Anomaly detection right now suffers from determining if noise is random or anomalous.

### Representative Model Outputs
Communicate uncertainty.  Communicate honsetly.

### Hidden Functionality
"Backdoors" exist in most ML systems, where particular circumstances can lead to detrimental results.  They differ from adversarial examples because they are inserted by bad actors at training time, not test time.  One way of making a backdoor is by "poisoning" images/text/data on the internet with your own data.  Getting rid of hidden functionality will likely be a constant competition between white-hat and black-hat ML hackers.


## Alignment
Okay, I'm done writing so much in a "summary".  From now on, only the biggest headings get text.

This section consists of lots of opaque/circular/vague methods to solve problems that may come up in the future regarding alignment.  E.g., the authors write, "To get a sense of an agent’s values and see how it make tradeoffs between values, researchers could also create diverse environments that capture realistic morally salient scenarios and characterize the choices that agents make when faced with ethical quandaries."  Why couldn't the authors just write, "Researchers could give the agents ethical dillemas to test their morals?"

## Systemic Safety
Machine learning can eventually be used to hack, and this is dangerous and needs to be countered with machine learning.  We also need to make sure our ML models aren't hacked, because (1) they could be dangerous in the hands of the public and (2) they could be subverted to give incorrect answers.

## Weaknesses
- This paper doesn't really address any *actual* solutions to any of the problems it presents.  I guess that's why it's titled "**Unsolved** Problems in ML Safety".
- There's much less of an emphasis on securing models that could be dangerous in the hands of the public than there should be.  E.g., The weights for a model that can create RNA sequences from desired protein folds should probably not be published on Github for any bad actor to download and design superviruses.  "Unsolved Problems in ML Safety" makes no mention on restricting such information.