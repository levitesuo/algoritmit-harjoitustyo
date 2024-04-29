from .objects.doubly_linked_list import LinkedList


def fringe_search(start, goal, node_list, heurestic_function):
    '''
    Finds the best path in node_list. Returns a dict with {'cost': , 'path': , 'closed_list': }

        Parameters:
            start (int): A integer indicating from where on the node list to start.
            goal (int): A integer indicating a goal in the node_list.
            node_list (list): List of nodes that have verticies and some values. (See src/algorithms/objects/node.py)
            heurestic_function (function): a function that takes in three inputs (position, goal, node_list) and spits out a heurestic estimate for the length of the route.

        Returns:
            Result (dict): A dictionary containing path, cost and closed_list aka. visited cells.
    '''
    size = len(node_list)
    fringe = LinkedList(size, start)
    cache = [False for _ in range(size)]

    cache[start] = (0, None)
    node_list[start].h = heurestic_function(node_list, start, goal)
    f_lim = node_list[start].h

    found = False

    while found is False or fringe.empty():
        f_min = float('inf')
        # Linked list has a default start node at size ** 2
        fringe.i = size
        while fringe.iterate():
            n = fringe.i
            g, _ = cache[n]
            f = g + node_list[n].h
            if f > f_lim:
                f_min = min(f, f_min)
                continue
            if n == goal:
                found = True
                break
            for i in range(len(node_list[n].edges) - 1, -1, -1):
                cost, s = node_list[n].edges[i]
                g_s = g + cost
                if cache[s]:
                    g_c, _ = cache[s]
                    if g_s >= g_c:
                        continue
                else:
                    node_list[s].h = heurestic_function(node_list, s, goal)
                fringe.delete_if_able(s)
                fringe.insert_after(s)
                cache[s] = (g_s, n)
            fringe.delete_current()
        f_lim = f_min
    if found:
        path = [goal]
        _, parent = cache[goal]
        while parent is not None:
            path.append(parent)
            _, new_parent = cache[parent]
            parent = new_parent
        return {'path': path, 'cost': g, 'cache': cache}
