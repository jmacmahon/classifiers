from .classifier import Classifier

import numpy as np
from scipy.stats import norm, multivariate_normal

WINES = np.loadtxt("wines.dat", delimiter=',')

def make_model(data):
    mean = np.mean(data[:, 1:], axis=0)
    covariance = np.cov(data[:, 1:], rowvar=0)
    return multivariate_normal(mean=mean, cov=covariance), len(data)

def classify(x, models):
    ps = []
    for model in models:
        p = model[0].pdf(x) * model[1]
        name = model[2]
        ps.append((p, name))
    return max(ps)[1]
