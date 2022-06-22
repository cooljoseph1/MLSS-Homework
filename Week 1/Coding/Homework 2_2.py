
##################
#   Constants    #
##################

D = 784 # 28 * 28
K = 10 # 0, 1, 2, ..., 9
N = 10 # arbitrary


def Estep(Xs, p, mix_p):
    """
    Xs -- N x D matrix of input data
    p -- K x D matrix of Bernoulli parameters
    mix_p -- K x 1 vector denoting how likely each row of p is
    """
    log_p = numpy.log(p)
    log_q = numpy.log(1 - p)
    log_mix_p = numpy.log(mix_p)

    eta = numpy.zeros((N, K))
    
    for i in range(len(Xs)):
        likelihoods = x[i, None, :] * log_p + (1 - x[i, None, :]) * log_q
        denominator = numpy.sum(likelihoods, axis=-1)
        eta[i] = log_mix_p + likelihoods - denominator

    return eta
