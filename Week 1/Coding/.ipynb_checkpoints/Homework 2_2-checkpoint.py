import numpy
from scipy.special import logsumexp
import matplotlib.pyplot as plt


#########################
#       Load Data       #
#########################
Xs = numpy.load("mnist_images.npy")

#########################
#       Constants       #
#########################
N, D = Xs.shape
K = 10 # 0, 1, 2, ..., 9


### For debugging purposes, only run with 100 images
N = 100
numpy.random.seed(1000)
Xs = Xs[numpy.random.randint(len(Xs), size=N)]



def Estep(Xs, p, mix_p):
    """
    Xs -- N x D matrix of input data
    p -- K x D matrix of Bernoulli parameters
    mix_p -- K x 1 vector denoting how likely each row of p is

    Note:  This function returns log(eta), not eta for purposes of
    numerical stability.
    """
    log_p = numpy.log(p)
    log_q = numpy.log(1 - p)
    log_mix_p = numpy.log(mix_p)

    eta = numpy.zeros((N, K))
    
    for i in range(N):
        likelihoods = Xs[i, None, :] * log_p + (1 - Xs[i, None, :]) * log_q
        likelihoods = numpy.sum(likelihoods, axis=-1)
        denominator = logsumexp(likelihoods)
        eta[i] = log_mix_p + likelihoods - denominator
    return eta

def Mstep(Xs, p, mix_p, alpha1, alpha2):

p = numpy.random.rand(K, D)
mix_p = numpy.random.rand(K)
mix_p /= numpy.sum(mix_p)

print(Estep(Xs, p, mix_p))
