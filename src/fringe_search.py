from math import sqrt
import time
from high_map_func import height_mapping_function
from node import Node
from doubly_linked_list import LinkedList


def heurestic_function(grid, cord: int, goal: int):
    '''
    Gives an estimate of cost from a point to the goal.
    '''
    s = len(grid)
    g_0 = goal // s
    g_1 = goal % s
    c_0 = cord // s
    c_1 = cord % s
    x_diff = g_0 // s - c_0
    y_diff = g_1 // s - c_1
    z_diff = grid[g_0][g_1] - \
        grid[g_0][g_1]

    return sqrt(x_diff**2+y_diff**2+z_diff**2)


def fringe_search(start_cord, goal_cord, grid):
    size = len(grid)
    start = start_cord[0]*size + start_cord[1]
    goal = goal_cord[0]*size + goal_cord[1]

    nodes = [Node((i // size, i % size), grid,
                  height_mapping_function) for i in range(size**2)]

    heurestics = [heurestic_function(grid, i, goal) for i in range(size ** 2)]
    fringe = LinkedList(size, start_cord)
    cache = [False for i in range(size ** 2)]
    cache[start] = (0, None)
    f_lim = heurestics[start]
    found = False
    start_time = time.time()
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
        end_time = time.time()
        # CONSTRUCT PATH AND CALCULATE LENGTH
        print("FOUND")
        path = []
        p_cost = 0
        _, parent = cache[goal]
        while parent is not None:
            path.append((parent // size, parent % size))
            _, new_parent = cache[parent]
            if new_parent:
                for edge in nodes[new_parent].fedges:
                    if edge[1] == parent:
                        p_cost += edge[0]
            parent = new_parent
        return {'path': path, 'cost': p_cost, 'cache': cache, 'time': end_time-start_time}
