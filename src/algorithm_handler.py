from time import time
from drawing_functions.draw_path import draw_path
from drawing_functions.draw_point_map import draw_pointmap


def algorithm_handler(name, color, data_map, algorithm, figure, is_fringe=False):

    start_time = time()
    result = algorithm()
    stop_time = time()

    if is_fringe:
        closed = []
        for n in range(len(result['cache'])):
            if result['cache'][n]:
                closed.append(result['cache'][n][0])
            else:
                closed.append(None)
        result['closed'] = closed

    print(
        f"{name + ' ' * (20 - len(name))} time: {stop_time-start_time}\t cost: {result['cost']}")

    draw_path(name, result['path'], data_map, color, figure)
    draw_pointmap(name + " visited", result['closed'], data_map, 'Bluered_r',
                  figure, result['path'][-1], result['path'][0])
