import plotly.graph_objects as go

from .draw_path import draw_path
from .draw_point_map import draw_pointmap


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
