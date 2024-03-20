import math
import heapq
from node import Node


def height_mapping_function(height_diff):
    a = 100
    if height_diff < -0.1:
        return height_diff * -5 * a + 0.5 + 1
    return height_diff * 20 * a + 3 + 1


def get_node_grid(grid):
    return [[Node((i, j), grid, height_mapping_function) for j in range(len(grid))] for i in range(len(grid))]


def if_in_grid(x, y, grid):
    width = len(grid)
    height = len(grid[0])
    return 0 <= x < width and 0 <= y < height


def h_function(x_pos, y_pos, x_goal, y_goal, grid):
    length = math.sqrt((x_pos-x_goal) ** 2 + (y_pos-y_goal) ** 2)
    return length


def trace_path(node_map, goal):
    path = []

    parent = goal
    while parent != (0, 0):
        path.append(parent)
        parent = node_map[parent[0]][parent[1]].parent
        if parent in path:
            print("ERROR: LOOP IN PAHT")
            return path
    return path


def a_star(start, goal, grid):
    width = len(grid)
    height = len(grid[0])

    visited_cells = [[False for _ in range(height)] for _ in range(width)]
    nodes = get_node_grid(grid)

    i = start[0]
    j = start[1]

    nodes[i][j].f = 0
    nodes[i][j].g = 0
    nodes[i][j].h = 0
    nodes[i][j].parrent = (i, j)

    open_list = []
    heapq.heappush(open_list, (0, i, j))

    found_dest = False
    with open('log.txt', 'w') as file:
        file.write("")
    while len(open_list) > 0:
        p = heapq.heappop(open_list)

        i = p[1]
        j = p[2]
        visited_cells[i][j] = True

        directions = [(0, 1), (0, -1), (1, 0), (-1, 0),
                      (1, 1), (1, -1), (-1, 1), (-1, -1)]
        for dir in directions:
            new_i = i + dir[0]
            new_j = j + dir[1]

            if if_in_grid(new_i, new_j, grid) and not visited_cells[new_i][new_j]:
                if (new_i, new_j) == goal:
                    nodes[new_i][new_j].parent = (i, j)
                    print("Destination found")
                    return [trace_path(nodes, goal), visited_cells]
                else:
                    new_g = nodes[i][j].g + \
                        nodes[i][j].edges[dir[0]+1][dir[1]+1]
                    new_h = h_function(new_i, new_j, goal[0], goal[1], grid)
                    new_f = new_g + new_h
                    if nodes[new_i][new_j].f == float('inf') or nodes[new_i][new_j].f > new_f:
                        heapq.heappush(open_list, (new_f, new_i, new_j))
                        with open('log.txt', 'a') as file:
                            file.write(
                                f"node: ({i}, {j})\tnewNode: ({new_i}, {new_j})\tnew_g: {new_g} \tnew_h: {new_h}\n")
                        nodes[new_i][new_j].f = new_f
                        nodes[new_i][new_j].g = new_g
                        nodes[new_i][new_j].h = new_h
                        nodes[new_i][new_j].parent = (i, j)
