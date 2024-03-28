from heapq import heappop, heappush
from heurestic_function import heurestic_function
from node import Node


def find_path(goal, nodes, size):
    path = []
    parent = nodes[goal].parent
    while parent != None:
        path.append((parent//size, parent % size))
        parent = nodes[parent].parent
    return {'path': path, 'cost': nodes[goal].g}


def a_star(start_cord, goal_cord, grid, h_func=heurestic_function):
    size = len(grid)
    start = start_cord[0]*size + start_cord[1]
    goal = goal_cord[0] * size + goal_cord[1]
    closed_list = [False for i in range(size ** 2)]
    open_list = []
    nodes = [Node((i//size, i % size), grid)
             for i in range(size ** 2)]

    nodes[start].g = 0
    heappush(open_list, (0, start))
    while len(open_list) != 0:
        g, p = heappop(open_list)
        closed_list[p] = nodes[p].f
        for edge in nodes[p].fedges:
            ng, np = edge
            if not closed_list[np]:
                if goal == np:
                    nodes[np].g = ng + g
                    nodes[np].parent = p
                    result = find_path(goal, nodes, size)
                    result['closed'] = closed_list
                    return result
                new_g = ng + g
                h = h_func(grid, np, goal)
                if nodes[np].f == float('inf') or nodes[np].f > new_g + h:
                    heappush(open_list, (new_g+h, np))
                    nodes[np].f = new_g + h
                    nodes[np].g = new_g
                    nodes[np].parent = p
    return False
