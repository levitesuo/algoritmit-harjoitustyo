import plotly.graph_objects as go


def draw_plain(surface):
    fig = go.Figure(
        data=[go.Surface(z=surface, showscale=False, name='Surface')])
    return fig
