from math import sqrt
from random import randint, seed
from perlin_noise import PerlinNoise


def layered_noise(random_seed, x, y, octaves=(1, 5), amplitudes=(1, 0.2)):
    result = 1
    seed(random_seed)
    for i in range(len(octaves)):
        result += PerlinNoise(octaves=octaves[i],
                              seed=randint(1, 1000))([x, y]) * amplitudes[i]
    return result


def hill_func(x, y):
    def helpper(p):
        return (1-p)**2 * (1+p)**2
    if -0.1 < x < 0.1:
        return 0
    return helpper(min(1, sqrt(x**2 + y**2)))


def plane_function(x, y):
    return 1


def slope_function(x, y):
    return x


def zig_zag_plane_function(x, y):
    if x < -0.5:
        return x
    if x < 0:
        return -1 - x
    if x < 0.5:
        return -1 + x
    return -x


def corridor_function(x, y):
    if 0.8 < x < 0.9:
        return 0
    if -0.9 < y < -0.8:
        return 0
    return randint(0, 100) / 100
