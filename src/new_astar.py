from heapq import heappop, heappush
from high_map_func import height_mapping_function
from node import Node


def heurestic_function(grid, cord: int, goal: int):
    '''
    Gives an estimate of cost from a point to the goal.
    '''
    s = len(grid)
    g_0 = goal // s
    g_1 = goal % s
    c_0 = cord // s
    c_1 = cord % s
    x_diff = g_0 // s - c_0
    y_diff = g_1 // s - c_1
    z_diff = grid[g_0][g_1] - \
        grid[g_0][g_1]

    return sqrt(x_diff**2+y_diff**2+z_diff**2)


def a_star(start_cord, goal_cord, grid, heurestic_function=heurestic_function):
    size = len(grid)
    start = start_cord[0] * size + start_cord[1]
    goal = goal_cord[0] * size + goal_cord[1]
    closed_list = [False for i in range(size ** 2)]
    open_list = []
    nodes = [Node((i//size, i % size), grid, height_mapping_function)
             for i in range(size ** 2)]
    found = False
