import numpy as np


def function2(vector):
    x1 = vector[0]
    x2 = vector[1]

    result = 1.5 - np.exp(-np.power(x1, 2) - np.power(x2, 2)) - 0.5 * np.exp(-np.power(x1 - 1, 2) - np.power(x2 + 2, 2))
    return result


def grad2(vector):
    x1 = vector[0]
    x2 = vector[1]

    result = np.array([2 * x1 * np.exp(-np.power(x1, 2) - np.power(x2, 2)) + (x1 - 1) * np.exp(
        -np.power(x1 - 1, 2) - np.power(x2 + 2, 2)),
                       2 * x2 * np.exp(-np.power(x1, 2) - np.power(x2, 2)) + (x2 + 2) * np.exp(
                           -np.power(x1 - 1, 2) - np.power(x2 + 2, 2))])
    return result
