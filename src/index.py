from random import randint as rnd
import time
import plotly.graph_objects as go
import plotly.express as px
import numpy as np
import pandas as pd
from perlin_noise import PerlinNoise
from a_star_class import AStar

# Defining a datamap from perlin noise.
noise1 = PerlinNoise(octaves=1, seed=rnd(1, 100))
noise2 = PerlinNoise(octaves=5, seed=rnd(1, 100))
# Defining x, y, z axels in 3d space.
data_resolution = 150
line_x = np.linspace(0, 1, data_resolution)
line_y = np.linspace(0, 1, data_resolution)
x, y = np.meshgrid(line_x, line_y)
z = np.array([[noise1([i, j]) + noise2([i, j])/5 for i, j in zip(xrow, yrow)]
             for xrow, yrow in zip(x, y)])

a_star = AStar()

start = (rnd(0, data_resolution - 1), 10)
goal = (rnd(0, data_resolution - 1), data_resolution - 10)
a_star.init(start, goal, z)

xx = []
yy = []
zz = []
df = px.data.iris()

path = a_star.get_path()

xx = np.array([cord[1] for cord in path])
yy = np.array([cord[0] for cord in path])
zz = []

for cord in path:
    zz.append(z[cord[0]][cord[1]]+0.01)

path_trace = go.Scatter3d(
    x=xx, y=yy, z=np.array(zz), line=dict(
        color='darkolivegreen',
        width=0.1
    ), marker=dict(
        size=0
    )
)
fig = go.Figure(data=[go.Surface(z=z)]).add_scatter3d(
    arg=path_trace, connectgaps=False)
fig.update_layout(autosize=False, width=500, height=500)
fig.show()
