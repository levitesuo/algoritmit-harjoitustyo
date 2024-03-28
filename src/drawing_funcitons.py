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


def draw_plots(surface, a_star_result, dijk_star_result, fringe_result, start, goal):
    fig = go.Figure(
        data=[go.Surface(z=surface, showscale=False, name='Surface')])
    draw_path('A*', a_star_result['path'], surface, 'green', fig)
    draw_pointmap('A* closed',
                  a_star_result['closed'], surface, 'Bluered_r', fig, start, goal)

    draw_path('D*', dijk_star_result['path'], surface, 'blue', fig)
    draw_pointmap('D* closed',
                  dijk_star_result['closed'], surface, 'Bluered_r', fig, start, goal)

    draw_path('FS', fringe_result['path'], surface, 'red', fig)
    f_closed = []
    for n in range(len(fringe_result['cache'])):
        if fringe_result['cache'][n]:
            f_closed.append(fringe_result['cache'][n][0])
        else:
            f_closed.append(None)

    draw_pointmap('FS closed',
                  f_closed, surface, 'Bluered_r', fig, start, goal)

    fig.update_layout(autosize=True, template='plotly_dark')
    fig.show()
