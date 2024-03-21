from math import sqrt
from random import randint as rnd
import numpy as np
from perlin_noise import PerlinNoise
from a_star import AStar


def heurestic_function(grid, goal: tuple, cord: tuple):
    '''
    Gives an estimate of cost from a point to the goal.
    '''
    x_diff = goal[0] - cord[0]
    y_diff = goal[1] - cord[1]
    z_diff = grid[goal[0]][goal[1]] - \
        grid[cord[0]][cord[1]]
    return sqrt(x_diff**2+y_diff**2+z_diff**2)


# Defining a datamap from perlin noise.
seed1 = rnd(1, 100)
seed2 = rnd(1, 100)

noise1 = PerlinNoise(octaves=1, seed=seed1)
noise2 = PerlinNoise(octaves=5, seed=seed2)
# Defining x, y, z axels in 3d space.
data_resolution = 50
line_x = np.linspace(0, 1, data_resolution)
line_y = np.linspace(0, 1, data_resolution)
x, y = np.meshgrid(line_x, line_y)
z = np.array([[noise1([i, j]) + noise2([i, j])/5 for i, j in zip(xrow, yrow)]
             for xrow, yrow in zip(x, y)])

a_star = AStar()
fails = 0
for i in range(data_resolution):
    print(i)
    for j in range(data_resolution):
        for ii in range(data_resolution):
            for jj in range(data_resolution):
                if (i, j) != (ii, jj):
                    start = (i, j)
                    goal = (ii, jj)
                    if a_star.init(start, goal, z):
                        if a_star.get_path():
                            if a_star.get_path_length() > heurestic_function(z, goal, start):
                                print(
                                    f"Heurestic function is bigger by {a_star.get_path_length() - heurestic_function(z, goal, start)}")
                                fails += 1
                    print(f"Fails: {fails}")
