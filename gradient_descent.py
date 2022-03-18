import numpy as np
from math import *


def calculate_function_minimum_from_input():
    variables = input("Enter all function variables separated with a comma: ")
    function_definition = input("Enter the function, which minimum will be calculated: ")
    function = eval("lambda {0}: {1}".format(variables, function_definition))
    gradient_definition = input("Enter the function's gradient: ")
    gradient = eval("lambda {0}: {1}".format(variables, gradient_definition))
    starting_point = float(input("Enter the starting point: "))
    step = float(input("Enter the step: "))
    reduction_param = float(input("Enter the reduction parameter: "))
    loop_limit = float(input("Enter the number of loops: "))
    eps = float(input("Enter the precision: "))

    return function, gradient, starting_point, step, reduction_param, loop_limit, eps


def calculate_function_minimum(function, gradient, starting_point, step, reduction_param, loop_limit, eps):
    x = starting_point
    loop_counter = 0

    while True:
        value = function(x)
        gradient_value = gradient(x)
        direction = -1 * gradient_value

        x_next = x + np.multiply(step, direction)
        next_value = function(x_next)

        if next_value >= value:
            step = step * reduction_param
            loop_counter = loop_counter + 1
            if loop_counter > loop_limit:
                break
        else:
            gradient_value_next = gradient(x_next)
            if np.linalg.norm(gradient_value_next) <= eps:
                break
            loop_counter = 0
            x = x_next

    return x
