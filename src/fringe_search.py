from math import sqrt
from high_map_func import height_mapping_function
from node import Node
from doubly_linked_list import LinkedList


def heurestic_function(grid, cord: tuple, goal: tuple):
    '''
    Gives an estimate of cost from a point to the goal.
    '''
    x_diff = goal[0] - cord[0]
    y_diff = goal[1] - cord[1]
    z_diff = grid[goal[0]][goal[1]] - \
        grid[cord[0]][cord[1]]

    return sqrt(x_diff**2+y_diff**2+z_diff**2)


def fringe_search(start, goal, grid):
    nodes = [[Node((i, j), grid, height_mapping_function)
              for i in range(len(grid))] for j in range(len(grid))]

    fringe = LinkedList(len(grid), start)
    cache = [[False for _ in range(len(grid))] for _ in range(len(grid))]
    cache[start[0]][start[1]] = (0, None)
    f_lim = heurestic_function(grid, start, goal)
    found = False
    while found is False or fringe.empty():
        f_min = float('inf')
        # Linked list has a default start node at size ** 2
        fringe.i = len(grid) ** 2
        while fringe.iterate():  # Returns false if at las on the list
            n = fringe.get_i()
            g, _ = cache[n[0]][n[1]]
            f = g + heurestic_function(grid, n, goal)
            if f > f_lim:
                f_min = min(f, f_min)
                continue
            if n == goal:
                found = True
                break
            for i in range(len(nodes[n[0]][n[1]].fedges) - 1, -1, -1):
                cost, s = nodes[n[0]][n[1]].fedges[i]
                g_s = g + cost
                if cache[s[0]][s[1]]:
                    g_c, _ = cache[s[0]][s[1]]
                    if g_s >= g_c:
                        continue
                fringe.delete_if_able(s)
                fringe.insert_after(s)
                cache[s[0]][s[1]] = (g_s, n)
            fringe.delete_current()
        f_lim = f_min
    if found:
        # CONSTRUCT PATH AND CALCULATE LENGTH
        print("FOUND")
        path = []
        p_cost = 0
        _, parent = cache[goal[0]][goal[1]]
        while parent is not None:
            path.append(parent)
            _, new_parent = cache[parent[0]][parent[1]]
            if new_parent:
                edge = (parent[0]-new_parent[0] + 1,
                        parent[1]-new_parent[1] + 1)
                p_cost += nodes[new_parent[0]
                                ][new_parent[1]].edges[edge[0]][edge[1]]
            parent = new_parent
        return {'path': path, 'cost': p_cost, 'cache': cache}
