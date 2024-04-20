class Node:
    def __init__(self):
        self.parent = None
        self.edges = []

        self.f = float('inf')
        self.g = float('inf')
        self.h = 0

    def init_edges(self, grid, pos, size, height_mapping_function, is_frigne=False):
        x = pos // size
        y = pos % size
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
                    self.edges.append((edge, new_x * size + new_y))
        if is_frigne:
            self.edges = sorted(self.edges)
