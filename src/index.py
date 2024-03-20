from random import randint as rnd
import plotly.graph_objects as go
import numpy as np
from perlin_noise import PerlinNoise
from a_star_class import AStar

# Defining a datamap from perlin noise.
noise = PerlinNoise(octaves=4, seed=rnd(1, 100))
# Defining x, y, z axels in 3d space.
data_resolution = 50
line_x = np.linspace(0, 1, data_resolution)
line_y = np.linspace(0, 1, data_resolution)
x, y = np.meshgrid(line_x, line_y)
z = np.array([[noise([i, j]) for i, j in zip(xrow, yrow)]
             for xrow, yrow in zip(x, y)])

a_star = AStar()

start = (rnd(0, data_resolution - 1), 10)
goal = (rnd(0, data_resolution - 1), data_resolution - 10)
a_star.init(start, goal, z)

color_map = np.array([['#9bc2de'for _ in range(data_resolution)]
                      for _ in range(data_resolution)])
color_map[start[0]][start[1]] = '#ff5900'
color_map[goal[0]][goal[1]] = '#f700ff'

frames = np.array(color_map)

done = False
while not done:
    done = a_star.step()
    for i in range(data_resolution):
        for j in range(data_resolution):
            if (i, j) != goal and (i, j) != start:
                if a_star.closed_list[i][j]:
                    color_map[i][j] = '#69f542'
                else:
                    color_map[i][j] = '#737373'
    np.append(frames, color_map, axis=0)
    print("K")


fig = go.Figure(data=[go.Surface(z=z)])
fig.update_layout(autosize=False, width=500, height=500)

fig.show()
