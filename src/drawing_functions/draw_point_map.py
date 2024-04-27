from math import sqrt
import plotly.graph_objects as go


def draw_pointmap(name, pointmap, grid, colorscale, figure, start, goal):
    '''
    Draws a pointmap on specified canvas.

    Parameters:
        name (str): Name of the pointmap. Will be shown on screen.
        pointmap (array): 2d array of points to be drawn containing float values that correspond to color.
        grid (array): 2d array of floats corresponding to height. Used to draw the point at the correct y cordinate.
        colorscale (str): plotly colorscale keyword. Spesifiec the colorscale of the pointmap.
        figure (plotly obj): Plotly figure object. Used as the canvas to draw on.
        start and goal (tuple): These cordinates are excluded from the pointmap. Otherwise the color scaling dosen't work.
    '''

    p = [[], [], [], []]
    size = int(sqrt(len(pointmap)))
    cordmap = [[pointmap[i*size + j]
                for i in range(size)] for j in range(size)]

    for i in range(size):
        for j in range(size):
            if cordmap[j][i] and (j, i) != start and (j, i) != goal:
                p[0].append(i)
                p[1].append(j)
                p[2].append(grid[j][i] + 0.001)
                p[3].append(cordmap[j][i])

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
