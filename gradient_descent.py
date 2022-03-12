import numpy as np

def calculate_function_minimum_from_input():
    function
    gradient
    starting_point
    step
    reduction_param
    loop_limit
    eps



    x = starting_point
    k = 0

    while True:
        value = function(x)
        gradient_value = gradient(x)
        direction = -1 * gradient_value

        x_next = x + np.multiply(step, direction)
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


def calculate_function_minimum(function, gradient, starting_point, step, reduction_param, loop_limit, eps):
    x = starting_point
    k = 0

    while True:
        value = function(x)
        gradient_value = gradient(x)
        direction = -1 * gradient_value

        x_next = x + np.multiply(step, direction)
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
