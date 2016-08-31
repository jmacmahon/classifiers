from .classifier import Classifier
from .util import separate

import numpy as np
from scipy.stats import norm, multivariate_normal

class Bayesian(Classifier):
    def train(self, data):
        if (data == np.array([]) or
            len(data.shape) != 2 or
            data.shape[1] <= 1):
            raise ValueError("Data must be 2-dimensional with >1 column")

        separated_data, classes = separate(data)
        self._models = {}
        for class_ in classes:
            this_class = separated_data[class_]
            mean = np.mean(this_class[:, 1:], axis=0)
            covariance = np.cov(this_class[:, 1:], rowvar=0)
            self._models[class_] = multivariate_normal(mean=mean,
                                                       cov=covariance)


# WINES = np.loadtxt("wines.dat", delimiter=',')
#
# def make_model(data):
#     mean = np.mean(data[:, 1:], axis=0)
#     covariance = np.cov(data[:, 1:], rowvar=0)
#     return multivariate_normal(mean=mean, cov=covariance), len(data)
#
# def classify(x, models):
#     ps = []
#     for model in models:
#         p = model[0].pdf(x) * model[1]
#         name = model[2]
#         ps.append((p, name))
#     return max(ps)[1]
