import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from fun1 import function1, grad1
from gradient_descent import calculate_function_minimum

# =======================================function1==================================
number_of_points_1 = 30
step_array_1 = [0.01, 0.1, 1, 2]

starting_point_array_1 = [(np.random.uniform(0, 1) - 0.5) * 20 for i in range(0, number_of_points_1)]
starting_point_array_1.sort()
print("Points that were chosen:")
print(starting_point_array_1)

for i in range(len(step_array_1)):
    solutions_array_1 = list(
        map(lambda starting_point: calculate_function_minimum(function1, grad1, starting_point, step_array_1[i], 0.9,
                                                              15, 0.001),
            starting_point_array_1))

    df = pd.DataFrame(dict(
        x=starting_point_array_1,
        y=solutions_array_1
    ))

    plt.subplot(4, 1, i + 1)
    plt.plot(starting_point_array_1, solutions_array_1)
    plt.title("Chosen step: " + str(step_array_1[i]))
    plt.grid(visible=True)
    plt.scatter(starting_point_array_1, solutions_array_1, marker='o')
    plt.subplots_adjust(hspace=0.7)

plt.xlabel('Randomized points')
plt.ylabel('Calculated function minimum')
plt.show()
