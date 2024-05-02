from math import sqrt
from functions.two_d_heurestic import two_d_heurestics


def two_d_translator(start, goal, node_list, algorithm, heurestic=two_d_heurestics):
    '''
    A function that translates .map files to a readable format for the algorithms.
    Then translates the result back to cordinates.

    Parameters:
        start and goal (tuples): tuples of cordinates corresponding to the start and the goal of path.
        node_list (list of Node objects): Will be used as the map for the function.
        algorithm (function): A function that takes inputs start, goal and node_map.

    Returns:
        path (list): A list of tuples / cordinates corresponding to the shortest path.
    '''
    size = int(sqrt(len(node_list)))

    translated_start = start[1] * size + start[0]
    translated_goal = goal[1] * size + goal[0]

    result = algorithm(start=translated_start,
                       goal=translated_goal,
                       node_list=node_list,
                       heurestic_function=heurestic
                       )

    return result
