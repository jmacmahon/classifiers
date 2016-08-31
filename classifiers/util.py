import numpy as np

def separate(data):
    classes = np.unique(data[:, 0])
    return dict([(n, data[data[:, 0] == n, :]) for n in classes]), classes
