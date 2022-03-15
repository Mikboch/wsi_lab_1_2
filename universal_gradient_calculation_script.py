import numpy as np
from gradient_descent import calculate_function_minimum, calculate_function_minimum_from_input


function, gradient, starting_point, step, reduction_param, loop_limit, eps = calculate_function_minimum_from_input()
print(calculate_function_minimum(function, gradient, starting_point, step, reduction_param, loop_limit, eps))