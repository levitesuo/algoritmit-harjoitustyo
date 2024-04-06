from height_mapping_function import height_mapping_function


class Node:
    def __init__(self, pos: tuple, grid):
        self.parent = None
        self.fedges = []

        self.f = float('inf')
        self.g = float('inf')
        self.h = 0
        self._init_edges(grid, pos)

    def _init_edges(self, grid, pos):
        x = pos[0]
        y = pos[1]
        size = len(grid)
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
