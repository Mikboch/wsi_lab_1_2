import numpy as np
import pandas as pd
from plotly.subplots import make_subplots
import matplotlib.pyplot as plt

from fun1 import function1, grad1
from fun2 import function2, grad2
from gradient_descent import calculate_function_minimum

# for function visualisation: 1.5 - exp(-x^2 - y^2) - 0.5 * exp(-(x-1)^2 - (y+2)^2)

number_of_points_1 = 30

# =======================================function1==================================
step_array_1 = [0.01, 0.1, 1, 2]

starting_point_array_1 = [(np.random.uniform(0, 1) - 0.5) * 20 for i in range(0, number_of_points_1)]
starting_point_array_1.sort()
print(starting_point_array_1)

fig1 = make_subplots(rows=4, cols=1)

for i in range(len(step_array_1)):
    solutions_array_1 = list(
        map(lambda starting_point: calculate_function_minimum(function1, grad1, starting_point, step_array_1[i], 0.9, 15, 0.001),
            starting_point_array_1))

    df = pd.DataFrame(dict(
        x=starting_point_array_1,
        y=solutions_array_1
    ))


    plt.subplot(4,1,i+1)
    plt.plot(starting_point_array_1, solutions_array_1)
    plt.title("Chosen step: "+str(step_array_1[i]))
    plt.grid(visible=True)
    plt.scatter(starting_point_array_1, solutions_array_1, marker='o')
    plt.subplots_adjust(hspace=0.7)


plt.xlabel('Randomized points')
plt.ylabel('Calculated function minimum')
plt.show()


print('')
#===========================function2================================
number_of_points_2 = 10
starting_point_array_2 = []

for j in range(number_of_points_2):
    x1=(np.random.uniform(0, 1) - 0.5) * 6
    x2=(np.random.uniform(0, 1) - 0.5) * 6
    starting_point_array_2.append(np.array([x1, x2]))

print("Start values for function 2: ")
print(starting_point_array_2)
print('')

step_array_2 = [0.01, 0.1, 1, 2]

for i in range(len(step_array_2)):
    solutions_array_2 = list(
        map(lambda starting_point: calculate_function_minimum(function2, grad2, starting_point, step_array_2[i], 0.8, 15, 0.001),
            starting_point_array_2))
    print("Gradient descent for step: "+str(step_array_2[i]))
    print(solutions_array_2)



# starting_point_2 = np.array([1, -1.5])
# print(calculate_function_minimum(function2, grad2, starting_point_2, 1, 0.9, 5, 0.001))