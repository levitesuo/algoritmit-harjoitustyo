import math
import heapq


class Node:
    def __init__(self, x, y, grid):
        self._pos = (x, y)
        self.edges = [[0 for _ in range(3)] for _ in range(3)]
        self._grid = grid

        self.parent = (0, 0)
        self.f = float('inf')
        self.g = float('inf')
        self.h = 0
        self._init_edges()

    def _init_edges(self):
        x = self._pos[0]
        y = self._pos[1]
        size = len(self._grid)
        for i in range(-1, 2):
            if 0 <= x + i < size:
                for j in range(-1, 2):
                    if 0 <= y + j < size and not (i == 0 and j == 0):
                        self.edges[i][j] = self._speed_calc(x+i, y+j)

    def _speed_calc(self, x, y):
        return height_mapping(self._pos[0], self._pos[1], x, y, self._grid)


def height_mapping(x_pos, y_pos, x_goal, y_goal, grid):
    return heigt_mapping_function(grid[x_goal][y_goal] - grid[x_pos][y_pos])


def heigt_mapping_function(height_diff):
    a = 10
    if height_diff < 0:
        return height_diff * -1
    return (height_diff * a) ** 2


def get_node_grid(grid):
    return [[Node(i, j, grid) for j in range(len(grid))] for i in range(len(grid))]


def if_in_grid(x, y, grid):
    width = len(grid)
    height = len(grid[0])
    return 0 <= x < width and 0 <= y < height


def h_function(x_pos, y_pos, x_goal, y_goal, grid):
    length = math.sqrt((x_pos-x_goal) ** 2 + (y_pos-y_goal) ** 2)
    height_diff = grid[x_goal][y_goal] - grid[x_pos][y_pos]
    return heigt_mapping_function(height_diff / length) * length


def trace_path(cell_details, dest):
    print("The Path is ")
    path = []
    row = dest[1]
    col = dest[0]

    # Trace the path from destination to source using parent cells
    while not (cell_details[row][col].parent[0] == row and cell_details[row][col].parent[1] == col):
        path.append((row, col))
        temp_row = cell_details[row][col].parent[0]
        temp_col = cell_details[row][col].parent[1]
        row = temp_row
        col = temp_col

    # Add the source cell to the path
    path.append((row, col))
    # Reverse the path to get the path from source to destination
    path.reverse()

    # Print the path
    for i in path:
        print("->", i, end=" ")
    print()
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

    while len(open_list) > 0:
        p = heapq.heappop(open_list)

        i = p[1]
        j = p[2]

        directions = [(0, 1), (0, -1), (1, 0), (-1, 0),
                      (1, 1), (1, -1), (-1, 1), (-1, -1)]
        for dir in directions:
            new_i = i + dir[0]
            new_j = j + dir[1]
            visited_cells[i][j] = True
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

                    print(f"node: ({i}, {j}) new_g: {new_g}")
                    if nodes[new_i][new_j].f == float('inf') or nodes[new_i][new_j].f > new_f:
                        heapq.heappush(open_list, (new_f, new_i, new_j))
                        nodes[new_i][new_j].f = new_f
                        nodes[new_i][new_j].g = new_g
                        nodes[new_i][new_j].h = new_h
                        nodes[new_i][new_j].parent = (i, j)
                        print("KK")
