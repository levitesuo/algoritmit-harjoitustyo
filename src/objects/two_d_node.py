class TwoDNode:
    '''
    Custon node class for .map files.
    Functions a lot like the default node class. Different edge calculations.
    '''

    def __init__(self, position, grid):
        self.position = position
        self.height = 0
        self.parent = None
        self.edges = []

        self.f = float('inf')
        self.g = float('inf')
        self.h = 0
        if grid[self.position[1]][self.position[0]] == ".":
            self._init_edges(grid)

    def reset(self):
        self.parent = None
        self.f = float('inf')
        self.g = float('inf')
        self.h = 0

    def _init_edges(self, grid):
        g = [[char for char in row]for row in grid]
        g[self.position[1]][self.position[0]] = "X"

        d = [(1, 0), (0, -1), (-1, 0), (0, 1)]
        for i, dir in enumerate(d):
            new_x = dir[0]+self.position[0]
            new_y = dir[1]+self.position[1]
            if 0 <= new_x < len(grid) and 0 <= new_y < len(grid) and grid[new_y][new_x] == ".":
                self.edges.append((1, new_x * len(grid) + new_y))
                g[new_y][new_x] = "E"
            dia_x = new_x + d[i-1][0]
            dia_y = new_y + d[i-1][1]
            deg_x = d[i-1][0] + self.position[0]
            deg_y = d[i-1][1] + self.position[1]
            if 0 <= dia_x < len(grid) and 0 <= dia_y < len(grid) and grid[new_y][new_x] == "." and grid[deg_y][deg_x] == "." and grid[dia_y][dia_x] == ".":
                self.edges.append((1.41421356, dia_x * len(grid) + dia_y))
                g[dia_y][dia_x] = "D"
        self.edges = sorted(self.edges)
