from math import sqrt


def heurestic_function(grid, cord: int, goal: int, data_resolution):
    '''
    Gives an estimate of cost from a point to the goal.
    '''
    s = len(grid)
    g_0 = goal // s
    g_1 = goal % s
    c_0 = cord // s
    c_1 = cord % s
    x_diff = g_0 - c_0
    y_diff = g_1 - c_1
    z_diff = grid[g_1][g_0] - \
        grid[c_1][c_0]

    return sqrt(x_diff**2+y_diff**2+z_diff**2)
