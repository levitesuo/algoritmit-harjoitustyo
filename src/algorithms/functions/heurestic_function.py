from math import sqrt
from algorithms.functions.height_mapping_function import height_mapping_function


def heurestic_function(grid, cord: int, goal: int):
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
    z_diff = (grid[g_0][g_1] - grid[c_0][c_1])

    return sqrt(x_diff**2+y_diff**2) + height_mapping_function(z_diff, s)
