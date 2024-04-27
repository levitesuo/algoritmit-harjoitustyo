from math import sqrt
from algorithms.functions.height_mapping_function import height_mapping_function


def heurestic_function(node_list, cord: int, goal: int):
    '''
    Gives an estimate of cost from a point to the goal.
    '''
    x_diff = node_list[goal].position[1] - node_list[cord].position[1]
    y_diff = node_list[goal].position[0] - node_list[cord].position[0]
    z_diff = node_list[goal].height - node_list[cord].height

    return sqrt(x_diff**2+y_diff**2) + height_mapping_function(z_diff, sqrt(len(node_list)))
