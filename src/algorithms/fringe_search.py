

from .functions.height_mapping_function import height_mapping_function
from .functions.heurestic_function import heurestic_function
from .objects.doubly_linked_list import LinkedList


class Node:
    def __init__(self):
        self.parent = None
        self.fedges = []

        self.f = float('inf')
        self.g = float('inf')
        self.h = 0

    def init_edges(self, grid, pos, size):
        x = pos // size
        y = pos % size
        for i in range(3):
            for j in range(3):
                new_x = x + i - 1
                new_y = y + j - 1
                if 0 <= new_x < size and 0 <= new_y < size and not (i == 1 and j == 1):
                    if i - 1 != 0 and j - 1 != 0:
                        edge = height_mapping_function(
                            grid[new_x][new_y] - grid[x][y], len(grid)) * 1.42
                    else:
                        edge = height_mapping_function(
                            grid[new_x][new_y] - grid[x][y], len(grid))
                    self.fedges.append((edge, new_x * size + new_y))
        self.fedges = sorted(self.fedges)


def fringe_search(start_cord, goal_cord, grid):
    size = len(grid)
    start = start_cord[0]*size + start_cord[1]
    goal = goal_cord[0]*size + goal_cord[1]
    nodes = [Node() for i in range(size**2)]

    fringe = LinkedList(size, start_cord)
    cache = [False for i in range(size ** 2)]

    cache[start] = (0, None)
    nodes[start].init_edges(grid, start, size)
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
            for i in range(len(nodes[n].fedges) - 1, -1, -1):
                cost, s = nodes[n].fedges[i]
                g_s = g + cost
                if cache[s]:
                    g_c, _ = cache[s]
                    if g_s >= g_c:
                        continue
                else:
                    nodes[s].init_edges(grid, s, size)
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
