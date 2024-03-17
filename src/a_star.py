class Node:
    def __init__(self, x, y, grid):
        self._pos = (x, y)
        self.costs = [[0 for _ in range(3)] for _ in range(3)]
        self._grid = grid
        self._init_costs()

    def _init_costs(self):
        x = self._pos[0]
        y = self._pos[1]
        size = len(self._grid)
        for i in range(-1, 2):
            if 0 <= x + i < size:
                for j in range(-1, 2):
                    if 0 <= x + i < size and not (i == 0 and j == 0):
                        self.costs[i][j] = self._speed_calc(x+i, y+j)

    def _speed_calc(self, x, y):
        a = 1
        grid = self._grid
        return max(grid[x][y] - grid[self._pos[0]][self._pos[1]]) * a + 1, 1)

def get_node_grid(grid):
    return [[Node(i, j, grid) for j in range(len(grid))] for i in range(len(grid))]