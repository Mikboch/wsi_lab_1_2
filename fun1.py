import numpy as np


def function1(x):
    result = np.power(x, 4)
    return result


def grad1(x):
    result = 4 * np.power(x, 3)
    return result
