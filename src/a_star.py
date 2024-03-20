import math
import heapq


class Node:
    def __init__(self, x, y, grid, height_mapping_function):
        self._pos = (x, y)
        self.edges = [[0 for _ in range(3)] for _ in range(3)]
        self._grid = grid
        self._height_mapping_function = height_mapping_function

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
            for j in range(-1, 2):
                if 0 <= y + j < size and 0 <= x + i < size and not (i == 0 and j == 0):
                    self.edges[i+1][j+1] = self._height_mapping_function(
                        self._grid[x+i][y+j]-self._grid[x][y])
                else:
                    self.edges[i+1][j+1] = float('inf')
        print(self.edges)


def height_mapping_function(height_diff):
    a = 10
    if height_diff < -0.1:
        return height_diff * -5 + 0.5 + 1
    return (height_diff * a) * 20 + 3 + 1


def get_node_grid(grid):
    return [[Node(i, j, grid, height_mapping_function) for j in range(len(grid))] for i in range(len(grid))]


def if_in_grid(x, y, grid):
    width = len(grid)
    height = len(grid[0])
    return 0 <= x < width and 0 <= y < height


def h_function(x_pos, y_pos, x_goal, y_goal, grid):
    length = math.sqrt((x_pos-x_goal) ** 2 + (y_pos-y_goal) ** 2)
    return length


def trace_path(cell_details, dest):
    print("The Path is ")
    path = []
    row = dest[0]
    col = dest[1]

    # Trace the path from destination to source using parent cells
    while not (cell_details[row][col].parent[0] == row and cell_details[row][col].parent[1] == col):
        path.append((row, col))
        temp_row = cell_details[row][col].parent[0]
        temp_col = cell_details[row][col].parent[1]
        row = temp_row
        col = temp_col
        if (row, col) in path:
            print("ERROR: LOOP IN PATH")
            return []

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
