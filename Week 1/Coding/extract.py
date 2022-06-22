from scipy.io import loadmat
import numpy

data = loadmat("mnist-original.mat")
labels = data["label"].transpose().flatten().astype(numpy.uint8)
numpy.save("mnist_labels.npy", labels)
