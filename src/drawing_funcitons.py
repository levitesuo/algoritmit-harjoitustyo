import plotly.graph_objects as go
import numpy as np


def path_trace(name, path, grid, color, figure):
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
