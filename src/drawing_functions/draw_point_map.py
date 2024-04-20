from math import sqrt
import plotly.graph_objects as go


def draw_pointmap(name, pointmap, grid, colorscale, figure, start, goal):
    p = [[], [], [], []]
    size = int(sqrt(len(pointmap)))
    cordmap = [[pointmap[i*size + j]
                for i in range(size)] for j in range(size)]

    for i in range(size):
        for j in range(size):
            if cordmap[i][j] and (i, j) != start and (i, j) != goal:
                p[0].append(i)
                p[1].append(j)
                p[2].append(grid[j][i] + 0.001)
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
