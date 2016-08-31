import pytest
import numpy as np

from .data import DATA_A

@pytest.fixture
def classifier():
    from classifiers.bayesian import Bayesian
    return Bayesian()

@pytest.mark.parametrize("data, means, covars", [DATA_A])
def test_train_correctness(classifier, data, means, covars):
    classifier.train(data)

    for class_ in means.keys():
        model = classifier._models[class_]
        mean_diff = abs(model.mean - means[class_])
        cov_diff = abs(model.cov - covars[class_])
        assert (mean_diff < 1e-10).all()
        assert (cov_diff < 1e-10).all()

@pytest.mark.parametrize("data", [
    np.array([]),
    np.array([[1], [1], [2]]),
])
def test_train_should_error_on_bad_input(classifier, data):
    with pytest.raises(ValueError) as exc_info:
        classifier.train(data)
    assert exc_info.value.args[0] == "Data must be 2-dimensional with >1 column"

def test_classify_method(classifier):
    pass
