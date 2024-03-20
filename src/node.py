class Node:
    def __init__(self, pos: tuple, grid, height_mapping_function):
        self.parent = (0, 0)
        self.edges = [[float('inf') for _ in range(3)] for _ in range(3)]

        self.f = float('inf')
        self.g = float('inf')
        self.h = 0
        self._init_edges(grid, pos, height_mapping_function)

    def _init_edges(self, grid, pos, height_mapping_function):
        x = pos[0]
        y = pos[1]
        size = len(grid)
        for i in range(3):
            for j in range(3):
                new_x = x + i - 1
                new_y = y + j - 1
                if 0 <= new_x < size and 0 <= new_y < size and not (i == 1 and j == 1):
                    self.edges[i][j] = height_mapping_function(
                        grid[new_x][new_y] - grid[x][y])
