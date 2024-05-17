SQRT2 = 1.41421356237309504880168872420969807856967187537694


class Node:
    def __init__(self, position, height, grid, height_mapping_function):
        self.position = position
        self.height = height
        self.parent = None
        self.edges = []

        self.f = float('inf')
        self.g = float('inf')
        self.h = 0

        self._init_edges(grid, height_mapping_function)

    def reset(self):
        self.parent = None
        self.f = float('inf')
        self.g = float('inf')
        self.h = 0

    def _init_edges(self, grid, height_mapping_function):
        x = self.position[1]
        y = self.position[0]
        for i in range(3):
            for j in range(3):
                new_x = x + i - 1
                new_y = y + j - 1
                if 0 <= new_x < len(grid[0]) and 0 <= new_y < len(grid) and not (i == 1 and j == 1):
                    if i - 1 != 0 and j - 1 != 0:
                        edge = abs(grid[new_y][new_x] - grid[y][x]) + SQRT2
                    else:
                        edge = abs(grid[new_y][new_x] - grid[y][x]) + 1
                    self.edges.append((edge, new_x * len(grid) + new_y))
            self.edges = sorted(self.edges)
