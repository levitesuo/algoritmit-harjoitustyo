from math import sqrt


def heurestic(node_list, cord: int, goal: int):
    '''
    Gives an estimate of cost from a point to the goal.
    '''
    x_diff = node_list[goal].position[1] - node_list[cord].position[1]
    y_diff = node_list[goal].position[0] - node_list[cord].position[0]
    z_diff = node_list[goal].height - node_list[cord].height

    return sqrt(x_diff**2+y_diff**2) + abs(z_diff) * sqrt(len(node_list)) + 1
