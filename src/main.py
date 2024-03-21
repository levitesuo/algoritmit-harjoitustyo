from random import randint as rnd
from matplotlib import pyplot as plt
from matplotlib import cm
from matplotlib.animation import FuncAnimation
import numpy as np
from perlin_noise import PerlinNoise
from a_star_class import AStar

# Defining a datamap from perlin noise.
noise = PerlinNoise(octaves=4, seed=rnd(1, 100))

# Defining x, y, z axels in 3d space.
data_resolution = 30
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


norm = plt.Normalize(z.min(), z.max())
colors = cm.viridis(norm(z))
r, c, _ = colors.shape

fig = plt.figure()
ax = fig.add_subplot(projection='3d')


def animate_graph(i):
    if not a_star.found:
        a_star.step()
        for i in range(data_resolution):
            for j in range(data_resolution):
                if a_star.closed_list[i][j]:
                    color_map[i][j] = '#69f542'
                else:
                    color_map[i][j] = '#737373'
    else:
        color_map[start[0]][start[1]] = '#ff5900'
        color_map[goal[0]][goal[1]] = '#f700ff'
    ax.plot_surface(x, y, z, facecolors=color_map)


ani = FuncAnimation(plt.gcf(), animate_graph, 1)
plt.show()
