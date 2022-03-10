import numpy as np
import plotly.express as px
import pandas as pd
from plotly.subplots import make_subplots
import plotly.graph_objects as go

from fun1 import function1, grad1
from fun2 import function2, grad2
from gradient_descent import calculate_function_minimum

# for function visualisation: 1.5 - exp(-x^2 - y^2) - 0.5 * exp(-(x-1)^2 - (y+2)^2)

number_of_points = 30
starting_point_array_1 = [(np.random.uniform(0, 1) - 0.5) * 40 for i in range(0, number_of_points)]

starting_point_array_1.sort()
solutions_array_1 = list(
    map(lambda starting_point: calculate_function_minimum(function1, grad1, starting_point, 0.1, 0.9, 150, 0.001),
        starting_point_array_1))

print(starting_point_array_1)
print(solutions_array_1)
print(calculate_function_minimum(function1, grad1, 1.58, 0.1, 0.9, 150, 0.001))
df = pd.DataFrame(dict(
    x=starting_point_array_1,
    y=solutions_array_1
))
print(df)
trace1 = px.line(data_frame=df, x="x", y="y", title="Function 1")
trace2 = px.scatter(x=starting_point_array_1, y=solutions_array_1)

fig1 = go.Figure(data=trace1.data + trace2.data)
fig1.update_traces(marker=dict(color='red'))
fig1.show()

print('')
starting_point_2 = np.array([1, -1.5])
print(calculate_function_minimum(function2, grad2, starting_point_2, 1, 0.9, 5, 0.001))

# fig = px.line(x=[1, 2, 3], y=[1, 2, 3])
# fig.show()
