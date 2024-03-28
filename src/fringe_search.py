from heurestic_function import heurestic_function
from node import Node
from doubly_linked_list import LinkedList


def fringe_search(start_cord, goal_cord, grid):
    size = len(grid)
    start = start_cord[0]*size + start_cord[1]
    goal = goal_cord[0]*size + goal_cord[1]

    nodes = [Node((i // size, i % size), grid) for i in range(size**2)]

    heurestics = [heurestic_function(grid, i, goal)
                  for i in range(size ** 2)]
    fringe = LinkedList(size, start_cord)
    cache = [False for i in range(size ** 2)]
    cache[start] = (0, None)
    f_lim = heurestics[start]
    found = False
    while found is False or fringe.empty():
        f_min = float('inf')
        # Linked list has a default start node at size ** 2
        fringe.i = size ** 2
        while fringe.iterate():  # Returns false if at las on the list
            n = fringe.i
            g, _ = cache[n]
            f = g + heurestics[n]
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
