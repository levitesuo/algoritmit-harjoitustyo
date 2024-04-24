from heapq import heappop, heappush
from .objects.node import Node
from .functions.heurestic_function import heurestic_function
from .functions.height_mapping_function import height_mapping_function


def find_path(goal, nodes, size):
    path = [(goal//size, goal % size)]
    parent = nodes[goal].parent
    while parent != None:
        path.append((parent//size, parent % size))
        parent = nodes[parent].parent

    cost = 0

    for i in range(len(path)):
        node = path[i][0] * size + path[i][1]
        for edge in nodes[node].edges:
            if i + 1 < len(path) and path[i+1][0]*size + path[i+1][1] == edge[1]:
                cost += edge[0]

    return {'path': path, 'cost': cost}


def a_star(start_cord, goal_cord, grid, heurestic_function=heurestic_function, height_mapping_function=height_mapping_function):
    size = len(grid)
    start = start_cord[0]*size + start_cord[1]
    goal = goal_cord[0] * size + goal_cord[1]
    closed_list = [False for i in range(size ** 2)]
    open_list = []
    nodes = [Node()
             for i in range(size ** 2)]

    nodes[start].g = 0
    heappush(open_list, (0, start))
    while len(open_list) != 0:
        _, p = heappop(open_list)
        nodes[p].init_edges(grid, p, size, height_mapping_function)
        g = nodes[p].g
        closed_list[p] = nodes[p].g + 1

        if goal == p:
            result = find_path(goal, nodes, size)
            result['closed'] = closed_list
            return result

        for edge in nodes[p].edges:
            cost, np = edge
            if not closed_list[np]:
                new_g = cost + g
                h = heurestic_function(grid, np, goal)
                new_f = h + new_g
                if nodes[np].f == float('inf') or nodes[np].f > new_f:
                    heappush(open_list, (new_f, np))
                    nodes[np].f = new_f
                    nodes[np].g = new_g
                    nodes[np].parent = p
    return False
