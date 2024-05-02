from math import sqrt


def two_d_heurestics(a, cord, goal):
    '''
    Heurestics function for .map files.
    Assumes the size of the grid is a square.
    '''
    size = int(sqrt(len(a)))
    x_diff = cord // size - goal // size
    y_diff = cord % size - goal % size
    return sqrt(x_diff**2 + y_diff**2)
