from random import randint, seed
from time import time
import plotly.graph_objects as go

from drawing_functions.draw_plots import draw_plots
from get_grid import get_grid
from algorithms.fringe_search import fringe_search
from algorithms.a_star import a_star

# Num of datapoint per side
data_resolution = 200

# Using randon seed so sitsuations are recreatable
# randomseed 9 weird
random_seed = randint(1, 1000)
print(f"RANDOM SEED: {random_seed}")
seed(random_seed)

# z is a  2d array where the values represent the hight
z = get_grid(data_resolution, random_seed)

# Random start and goal
start = (randint(1, data_resolution//2), 10)
goal = (randint(data_resolution//2, data_resolution-1), data_resolution-10)

print(f"start: {start}   goal: {goal}")

# Running the algorithms and measuring their performance
a_time = time()
a_star_result = a_star(start, goal, z)
b_time = time()
dijk_star_result = a_star(start, goal, z, lambda x, y, z: 0)
c_time = time()
fringe_result = fringe_search(start, goal, z)
d_time = time()

# Printing the stats
print(f"a* - t: {b_time-a_time}\tc: {a_star_result['cost']}")
print(f"d* - t: {c_time-b_time}\tc: {dijk_star_result['cost']}")
print(f"fs - t: {d_time-c_time}\tc: {fringe_result['cost']}")

# Drawing the visualization
draw_plots(z, a_star_result, dijk_star_result, fringe_result, start, goal)
