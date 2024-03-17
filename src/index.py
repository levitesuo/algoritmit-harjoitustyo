from mpl_toolkits import mplot3d
from matplotlib import pyplot
from matplotlib import cm
import numpy as np
from perlin_noise import PerlinNoise


noise = PerlinNoise(octaves=5, seed=1)
xpix, ypix = 100, 100
a = np.linspace(0, 1, 50)
b = np.linspace(0, 1, 50)
x, y = np.meshgrid(a, b)
z = np.array([[noise([i, j]) for i, j in zip(xrow, yrow)]
             for xrow, yrow in zip(x, y)])

norm = pyplot.Normalize(z.min(), z.max())
colors = cm.viridis(norm(z))
r, c, _ = colors.shape

fig = pyplot.figure()
wf = pyplot.axes(projection='3d')

wf.plot_surface(x, y, z, rcount=r, ccount=c, facecolors=colors, shade=False)

pyplot.axis('off')
pyplot.show()
