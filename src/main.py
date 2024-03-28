from random import randint, seed
from time import time
import plotly.graph_objects as go

from drawing_funcitons import path_trace
from get_grid import get_grid
from fringe_search import fringe_search
from new_astar import a_star

data_resolution = 200

random_seed = randint(1, 1000)
print(f"RANDOM SEED: {random_seed}")
seed(random_seed)


z = get_grid(data_resolution, random_seed)

start = (randint(1, data_resolution/2), 10)
goal = (randint(data_resolution/2, data_resolution-1), data_resolution-10)

a_time = time()
a_star_result = a_star(start, goal, z)
b_time = time()
dijk_star_result = a_star(start, goal, z, lambda x, y, z: 0)
c_time = time()
fringe_result = fringe_search(start, goal, z)
d_time = time()

print(f"a* - t: {b_time-a_time}       c: {a_star_result['cost']}")
print(f"d* - t: {c_time-b_time}       c: {dijk_star_result['cost']}")
print(f"fs - t: {d_time-c_time}       c: {fringe_result['cost']}")

fig = go.Figure(data=[go.Surface(z=z, showscale=False, name='Surface')])

path_trace('A_star', a_star_result['path'], z, 'green', fig)
path_trace('Dijk_star', dijk_star_result['path'], z, 'blue', fig)
path_trace('Fringe_search', fringe_result['path'], z, 'red', fig)

fig.update_layout(autosize=True, template='plotly_dark')
fig.show()
