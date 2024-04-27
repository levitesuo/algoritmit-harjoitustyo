from time import time
from drawing_functions.draw_path import draw_path
from drawing_functions.draw_point_map import draw_pointmap

from algorithms.objects.node import Node
from algorithms.functions.height_mapping_function import height_mapping_function


def algorithm_translator(start, goal, grid, algorithm):
    '''
    A function that translates the grids we are using to node_lists that the algorithms are using.

        Parameters:
            grid (array): 2d array containing floats that corrispond to heights.
            algorithm (function): A function that takes one input the map and is otherwise redy to run.

        Returns:
            The reusults of the algorithm, exept the paht has been translated to x, y cordinates and runtime has been added.
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


def algorithm_visualizer(name, color, data_map, start, goal, algorithm, figure, is_fringe=False):
    '''

    '''
    result = algorithm_translator(start, goal, data_map, algorithm)

    if is_fringe:
        closed = []
        for n in range(len(result['cache'])):
            if result['cache'][n]:
                closed.append(result['cache'][n][0])
            else:
                closed.append(None)
        result['closed'] = closed

    print(
        f"{name + ' ' * (20 - len(name))} time: {result['time']}\t cost: {result['cost']}")

    draw_path(name, result['path'], data_map, color, figure)
    draw_pointmap(name=name + " visited",
                  pointmap=result['closed'],
                  grid=data_map,
                  colorscale='Bluered_r',
                  figure=figure,
                  start=result['path'][-1],
                  goal=result['path'][0]
                  )
