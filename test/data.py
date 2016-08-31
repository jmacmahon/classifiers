from classifiers.util import separate
import numpy as np

def data_a():
    values = np.array([
        [0, 1],
        [0, 2],
        [0, 1],
        [0, 1],
        [0, 1],
        [1, 5],
        [1, 4],
        [1, 5],
        [1, 6]
    ])
    means = {0: np.array([1.2]), 1: np.array([5])}
    covars = {0: np.array(0.2), 1: np.array(2/3)}

    return (values, means, covars)

DATA_A = data_a()

def sanity_data_a():
    values = np.array([])
    means = {}
    covars = {}

    return (values, means, covars)
