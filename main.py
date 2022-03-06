import numpy as np


def function1(x):
    result = np.power(x, 4)
    return result


def grad1(x):
    result = 4 * np.power(x, 3)
    return result


# for function visualisation: 1.5 - exp(-x^2 - y^2) - 0.5 * exp(-(x-1)^2 - (y+2)^2)

def function2(vector):
    x1 = vector[0]
    x2 = vector[1]

    result = 1.5 - np.exp(-np.power(x1,2) - np.power(x2,2)) - 0.5*np.exp(-np.power(x1-1,2) - np.power(x2+2,2))
    return result


def grad2(vector):
    x1 = vector[0]
    x2 = vector[1]

    result = np.array([2*x1*np.exp(-np.power(x1,2) - np.power(x2,2)) + (x1-1)*np.exp(-np.power(x1-1,2) - np.power(x2+2,2)),
              2*x2*np.exp(-np.power(x1,2) - np.power(x2,2)) + (x2+2)*np.exp(-np.power(x1-1,2) - np.power(x2+2,2))])
    return result



def calculate_function_minimum(function, gradient, starting_point, step, reduction_param, loop_limit, eps):
    x = starting_point
    k = 0

    while True:
        value = function(x)
        gradient_value = gradient(x)
        direction = -1*gradient_value

        x_next = x + np.multiply(step,direction)
        next_value = function(x_next)

        if next_value >= value:
            step = step * reduction_param
            k = k + 1
            if k > loop_limit:
                break
        else:
            gradient_value_next = gradient(x_next)
            if np.linalg.norm(gradient_value_next) <= eps:
                break
            k = 0
            x = x_next

    return x

starting_point = 10

ans = calculate_function_minimum(function1, grad1, starting_point, 0.01, 0.9, 20, 0.001)
print(ans)


starting_point_2 = np.array([1,-1.5])
print(calculate_function_minimum(function2, grad2, starting_point_2, 1, 0.9, 5, 0.001))

