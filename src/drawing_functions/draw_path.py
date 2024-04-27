import numpy as np
import plotly.graph_objects as go


def draw_path(name, path, grid, color, figure):
    '''
    Draws a line and dots corresponding to the path list
        Parameters:
            name (str): Name of the path to be drawn. Will be shown on screen.
            path (list): List of tuples from which the line is drawn.
            grid (array): 2d array from where we check the y cordinate of points in path.
            figure (plotly.graph_objects figure): The base "canvas" where the path will be drawn.
    '''
    p = [[], [], []]
    for cord in path:
        p[0].append(cord[1])
        p[1].append(cord[0])
        p[2].append(grid[cord[0]][cord[1]]+0.005)
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
