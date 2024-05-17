from heapq import heappop, heappush


def find_path(node_list, goal):
    '''
    When the a* has found the goal this method is responsible for "retracing" a*:s steps.
        Parameter:
            node_list (list): List of node objects.
            goal (int): place of the goal in the node_list

        Returns:
            Result (dict): a dictionary with one key/value pari path.
    '''
    parent = goal
    path = []
    while parent is not None:
        path.append(parent)
        parent = node_list[parent].parent
        if parent in path:
            break
    return {'path': path}


def a_star(start, goal, node_list, heurestic_function):
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
    list_index = 0
    size = len(node_list)
    closed_list = [False for _ in range(size)]
    open_list = []
    node_list[start].g = 0
    heappush(open_list, (0, list_index, start))
    list_index -= 1
    while open_list:
        _, _, p = heappop(open_list)
        g = node_list[p].g
        closed_list[p] = node_list[p].g+1
        if goal == p:
            result = find_path(node_list, goal)
            result['cost'] = node_list[p].g
            result['closed'] = closed_list
            return result
        for cost, new_p in node_list[p].edges:
            if not closed_list[new_p]:
                new_g = cost + g
                h = heurestic_function(node_list[new_p], node_list[goal], size)
                new_f = h + new_g
                if node_list[new_p].f == float('inf') or node_list[new_p].f > new_f:
                    heappush(open_list, (new_f, list_index, new_p))
                    list_index -= 1
                    node_list[new_p].f = new_f
                    node_list[new_p].g = new_g
                    node_list[new_p].parent = p
    return False
