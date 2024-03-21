from random import randint as rnd
import plotly.graph_objects as go
import numpy as np
import pandas as pd
from perlin_noise import PerlinNoise
from a_star import AStar
from fringe_search import FringeSearch

# Defining a datamap from perlin noise.
seed1 = rnd(1, 100)
seed2 = rnd(1, 100)
print(f"seed1: {seed1}      seed2: {seed2}")
noise1 = PerlinNoise(octaves=1, seed=seed1)
noise2 = PerlinNoise(octaves=5, seed=seed2)
# Defining x, y, z axels in 3d space.
data_resolution = 100
line_x = np.linspace(0, 1, data_resolution)
line_y = np.linspace(0, 1, data_resolution)
x, y = np.meshgrid(line_x, line_y)
z = np.array([[noise1([i, j]) + noise2([i, j])/5 for i, j in zip(xrow, yrow)]
             for xrow, yrow in zip(x, y)])

a_star = AStar()
f_search = FringeSearch()

start = (rnd(0, data_resolution - 1), 10)
goal = (rnd(0, data_resolution - 1), data_resolution - 10)
a_star.init(start, goal, z)
f_search.init(start, goal, z)


xx = []
yy = []
zz = []
a_path = a_star.get_path()
path = f_search.get_path()

closed = [[], [], [], []]
for i in range(len(a_star.closed_list)):
    for j in range(len(a_star.closed_list)):
        if a_star.closed_list[i][j] and (i, j) != start and (i, j) != goal:
            closed[0].append(j)
            closed[1].append(i)
            closed[2].append(z[i][j] + 0.001)
            closed[3].append(a_star._nodes[i][j].f)


xx = np.array([cord[1] for cord in path])
yy = np.array([cord[0] for cord in path])
zz = []

for cord in path:
    zz.append(z[cord[0]][cord[1]]+0.002)

start_trace = go.Scatter3d(
    name='Start',
    x=[start[1]],
    y=[start[0]],
    z=[z[start[0]][start[1]]+0.002],
    marker=dict(
        color='red',
        size=5
    )
)

goal_trace = go.Scatter3d(
    name='Goal',
    x=[goal[1]],
    y=[goal[0]],
    z=[z[goal[0]][goal[1]]+0.002],
    marker=dict(
        color='purple',
        size=5
    )
)

closed_trace = go.Scatter3d(
    name='Visited nodes',
    x=closed[0],
    y=closed[1],
    z=closed[2],
    mode='markers',
    visible='legendonly',
    marker=dict(
        size=2,
        opacity=0.3,
        color=closed[3],
        colorbar=dict(
            title='F_value'
        ),
        colorscale='speed',
        cmin=min(closed[3]), cmax=max(closed[3]), cauto=False,
        showscale=False
    )
)

path_trace = go.Scatter3d(
    name='Path',
    x=xx,
    y=yy,
    z=np.array(zz),
    visible='legendonly',
    marker=dict(
        size=3,
        color='red'
    )
)

fig = go.Figure(data=[go.Surface(z=z, showscale=False)])
fig.add_scatter3d(arg=path_trace, connectgaps=False)
fig.add_scatter3d(arg=closed_trace, connectgaps=False)
fig.add_scatter3d(arg=start_trace, connectgaps=False)
fig.add_scatter3d(arg=goal_trace, connectgaps=False)
fig.update_layout(autosize=True, template='plotly_dark')

fig.show()
