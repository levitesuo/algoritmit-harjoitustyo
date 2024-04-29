from time import time
from algorithms.objects.node import Node
from algorithms.functions.height_mapping_function import height_mapping_function


def generated_map_translator(start, goal, grid, algorithm):
    '''

    A function that translates the grids we rae using to node_lists that the algorithms are using. 
    Also mesures the algorithm running time.
    THIS IS WHERE THE FUNCTION CALL FINALLY HAPPENS.

        Parameters:
            grid (array): 2d array containing floats that corrispond to heights.
            start and goal (tuples): tuples of cordinates corresponding to the start and the goal of path.
            algorithm (function): A function that takes inputs start, goal and node_map.

        Returns:
            result (dict): The reusults of the algorithm, exept the paht has been translated to x, y cordinates and runtime has been added.
    '''
    node_list = []
    for i in range(len(grid)*len(grid[0])):
        node_list.append(
            Node(
                position=(i % len(grid), i // len(grid)),
                height=grid[i % len(grid)][i // len(grid)],
                grid=grid,
                height_mapping_function=height_mapping_function))

    translated_start = start[1] * len(grid) + start[0]
    translated_goal = goal[1] * len(grid) + goal[0]

    start_time = time()
    result = algorithm(translated_start, translated_goal, node_list)
    end_time = time()

    translated_path = []
    for node in result['path']:
        translated_path.append((node % len(grid), node // len(grid)))

    result['path'] = translated_path
    result['time'] = end_time - start_time
    return result
