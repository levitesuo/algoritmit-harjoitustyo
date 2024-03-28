from random import seed, randint
import numpy as np
from perlin_noise import PerlinNoise


def get_grid(data_resolution, random_seed):
    seed(random_seed)
    seed1 = randint(1, 1000)
    seed2 = randint(1, 1000)

    noise1 = PerlinNoise(octaves=1, seed=seed1)
    noise2 = PerlinNoise(octaves=5, seed=seed2)

    line_x = np.linspace(0, 1, data_resolution)
    line_y = np.linspace(0, 1, data_resolution)
    x, y = np.meshgrid(line_x, line_y)
    z = np.array([[round(noise1([i, j]) + noise2([i, j])/5 + 0.5, 4) for i, j in zip(xrow, yrow)]
                  for xrow, yrow in zip(x, y)])
    return z
