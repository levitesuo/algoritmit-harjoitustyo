

from .functions.height_mapping_function import height_mapping_function
from .functions.heurestic_function import heurestic_function
from .objects.doubly_linked_list import LinkedList
from .objects.node import Node


def fringe_search(start_cord, goal_cord, grid, heurestic_function=heurestic_function, height_mapping_function=height_mapping_function):
    size = len(grid)
    start = start_cord[0]*size + start_cord[1]
    goal = goal_cord[0]*size + goal_cord[1]
    nodes = [Node() for i in range(size**2)]

    fringe = LinkedList(size, start_cord)
    cache = [False for i in range(size ** 2)]

    cache[start] = (0, None)
    nodes[start].init_edges(grid, start, size, height_mapping_function, True)
    nodes[start].h = heurestic_function(grid, start, goal)

    f_lim = nodes[start].h
    found = False

    while found is False or fringe.empty():
        f_min = float('inf')
        # Linked list has a default start node at size ** 2
        fringe.i = size ** 2
        while fringe.iterate():  # Returns false if at las on the list
            n = fringe.i
            g, _ = cache[n]
            f = g + nodes[n].h
            if f > f_lim:
                f_min = min(f, f_min)
                continue
            if n == goal:
                found = True
                break
            for i in range(len(nodes[n].edges) - 1, -1, -1):
                cost, s = nodes[n].edges[i]
                g_s = g + cost
                if cache[s]:
                    g_c, _ = cache[s]
                    if g_s >= g_c:
                        continue
                else:
                    nodes[s].init_edges(
                        grid, s, size, height_mapping_function, True)
                    nodes[s].h = heurestic_function(grid, s, goal)
                fringe.delete_if_able(s)
                fringe.insert_after(s)
                cache[s] = (g_s, n)
            fringe.delete_current()
        f_lim = f_min
    if found:
        # CONSTRUCT PATH
        path = [(goal//size, goal % size)]
        _, parent = cache[goal]
        while parent is not None:
            path.append((parent // size, parent % size))
            _, new_parent = cache[parent]
            parent = new_parent
        return {'path': path, 'cost': g, 'cache': cache}
