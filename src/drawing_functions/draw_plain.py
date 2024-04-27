import plotly.graph_objects as go


def draw_plain(surface):
    '''
    Draws a plain from the surface

        Parameters:
            surface (array): 2d array where values correspond with height.

        Returns:
            fig (figure obj)
    '''
    fig = go.Figure(
        data=[go.Surface(z=surface, showscale=False, name='Surface')])
    return fig
