from math import sqrt
import plotly.graph_objects as go
import numpy as np


def draw_path(name, path, grid, color, figure):
    p = [[], [], []]
    for cord in path:
        p[0].append(cord[0])
        p[1].append(cord[1])
        p[2].append(grid[cord[1]][cord[0]]+0.005)
    trace = go.Scatter3d(
        name=name,
        x=np.array(p[0]),
        y=np.array(p[1]),
        z=np.array(p[2]),
        marker=dict(
            size=3,
            color=color
        )
    )
    figure.add_scatter3d(arg=trace, connectgaps=False)
    return trace


def draw_pointmap(name, pointmap, grid, colorscale, figure, start, goal):
    p = [[], [], [], []]
    size = int(sqrt(len(pointmap)))
    cordmap = [[pointmap[i*size + j]
                for i in range(size)] for j in range(size)]

    for i in range(size):
        for j in range(size):
            if cordmap[i][j] and (i, j) != start and (i, j) != goal:
                p[0].append(j)
                p[1].append(i)
                p[2].append(grid[i][j] + 0.001)
                p[3].append(cordmap[i][j])

    trace = go.Scatter3d(
        name=name,
        x=p[0],
        y=p[1],
        z=p[2],
        mode='markers',
        visible='legendonly',
        marker=dict(
            size=4,
            opacity=0.3,
            color=p[3],
            colorbar=dict(
                title=name
            ),
            colorscale=colorscale,
            cmin=min(p[3]), cmax=max(p[3]), cauto=False,
            showscale=False
        )
    )
    figure.add_scatter3d(arg=trace, connectgaps=False)
