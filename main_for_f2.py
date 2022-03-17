import numpy as np
from fun2 import function2, grad2
from gradient_descent import calculate_function_minimum


# ===========================function2================================
# for function visualisation: 1.5 - exp(-x^2 - y^2) - 0.5 * exp(-(x-1)^2 - (y+2)^2)
number_of_points_2 = 10
starting_point_array_2 = []
starting_point_array_2.append(np.array([1.1, -2.1]))

# for j in range(number_of_points_2):
#     x1=(np.random.uniform(0, 1) - 0.5) * 6
#     x2=(np.random.uniform(0, 1) - 0.5) * 6
#     starting_point_array_2.append(np.array([x1, x2]))

print("Starting values:")
print(starting_point_array_2)
print('')

step_array_2 = [0.01, 0.1, 1, 10, 100, 1000]

for i in range(len(step_array_2)):
    solutions_array_2 = list(
        map(lambda starting_point: calculate_function_minimum(function2, grad2, starting_point, step_array_2[i], 0.8,
                                                              15, 0.001),
            starting_point_array_2))
    print("Gradient descent for step: " + str(step_array_2[i]))
    print(solutions_array_2)
