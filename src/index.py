from mpl_toolkits import mplot3d
from matplotlib import pyplot
from matplotlib import cm
import numpy as np
from perlin_noise import PerlinNoise
from a_star import a_star


noise = PerlinNoise(octaves=2, seed=2)
xpix, ypix = 100, 100
data_range = (0, 1)
point_ammount = 100
a = np.linspace(data_range[0], data_range[1], point_ammount)
b = np.linspace(data_range[0], data_range[1], point_ammount)
x, y = np.meshgrid(a, b)
z = np.array([[noise([i, j]) for i, j in zip(xrow, yrow)]
             for xrow, yrow in zip(x, y)])

norm = pyplot.Normalize(z.min(), z.max())
colors = cm.viridis(norm(z))
r, c, _ = colors.shape

fig = pyplot.figure()
bx = fig.add_subplot(111, projection='3d')  # , computed_zorder=False)
bx.plot_surface(x, y, z, rcount=r, ccount=c, facecolors=colors, shade=False)
# bx.plot_wireframe(x, y, z, zorder=0)
# wf = pyplot.axes(projection='3d')

data = a_star((10, 10), (90, 90), z)
path = data[0]
visited = data[1]

path_x = []
path_y = []
path_z = []


for cord in path:
    x_c = cord[0] / point_ammount * \
        (data_range[1]-data_range[0]) + data_range[0]
    y_c = cord[1] / point_ammount * \
        (data_range[1]-data_range[0]) + data_range[0]
    z_c = z[cord[0]][cord[1]]
    path_x.append(x_c)
    path_y.append(y_c)
    path_z.append(z_c)

bx.plot(path_x, path_y, path_z, zorder=10, color='red')
print(f"MAX_H: {max(path_z)}")

# pyplot.axis('off')
pyplot.show()
