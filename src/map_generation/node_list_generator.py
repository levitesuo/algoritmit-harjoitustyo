from functions.height_mapping import height_mapping
from objects.node import Node
from objects.two_d_node import TwoDNode


def node_list_generator(grid, use_two_d):
    '''
    A function for converting a grid or map to node list.

    Arguments:
        grid (array): Data to be converted
        use_two_d (bool): if the data is 2d

    Returns:
        node_list (list): a list of node objects.
    '''
    nodes = []
    if use_two_d:
        rows = grid.split("\n")[4:]
        rows.pop()
        for i in range(len(rows)):
            for j in range(len(rows)):
                nodes.append(TwoDNode((i, j), rows))
    else:
        for i in range(len(grid)*len(grid[0])):
            nodes.append(
                Node(
                    position=(i % len(grid), i // len(grid)),
                    height=grid[i % len(grid)][i // len(grid)],
                    grid=grid,
                    height_mapping_function=height_mapping))
    return nodes
