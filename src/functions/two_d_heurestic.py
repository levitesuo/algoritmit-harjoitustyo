from math import sqrt


def two_d_heurestics(start_node,  goal_node, size):
    '''
    Gives an estimate of cost from a point to the goal.
    '''
    x_diff = goal_node.position[1] - start_node.position[1]
    y_diff = goal_node.position[0] - start_node.position[0]

    return sqrt(x_diff**2 + y_diff**2)
