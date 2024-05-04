from map_generation.translator import translator
from drawing_functions.draw_path import draw_path
from drawing_functions.draw_point_map import draw_pointmap


def algorithm_handler(name, color, grid, node_list, start, goal, algorithm, figure, is_fringe=False):
    '''
    Handels the drawing, running and time measurements for a algorithm.
    '''
    result = translator(start, goal, node_list, algorithm)

    for node in node_list:
        node.reset()

    # Fringe searches visited cells are stored in a different format. the loop below transforms them.
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

    draw_path(name=name,
              path=result['path'],
              grid=grid,
              color=color,
              figure=figure
              )
    draw_pointmap(name=name + " visited",
                  pointmap=result['closed'],
                  grid=grid,
                  colorscale='Bluered_r',
                  figure=figure,
                  start=result['path'][-1],
                  goal=result['path'][0]
                  )
    return result
