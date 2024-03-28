import heapq
from math import sqrt
from node import Node
from height_mapping_function import height_mapping_function


class AStar:
    '''
        Solves the A* algorithm on a heightmap.
        Inputs are a grid wich is a square 2d array with values that represent their height.
        start and goal wich are cordinates in that map.
    '''

    def __init__(self):
        self.closed_list = []
        self.open_list = []
        self._nodes = []
        self._grid = None

        self.goal = None
        self.found = None

    def init(self, start, goal, grid):

        self.open_list = []
        self.found = False
        self._grid = grid
        size = len(grid)

        self.goal = goal
        self._nodes = [[Node((i, j), grid, height_mapping_function)
                        for i in range(size)] for j in range(size)]
        self.closed_list = [[False for _ in range(size)] for _ in range(size)]

        self._nodes[start[0]][start[1]].f = 0
        self._nodes[start[0]][start[1]].g = 0
        self._nodes[start[0]][start[1]].h = 0
        self._nodes[start[0]][start[1]].parent = (start[0], start[1])

        heapq.heappush(
            self.open_list, (0, (start[0], start[1]), self._nodes[start[0]][start[1]]))
        return True

    def step(self):
        p = heapq.heappop(self.open_list)

        i = p[1][0]
        j = p[1][1]

        self.closed_list[i][j] = True

        directions = [(0, 1), (0, -1), (1, 0), (-1, 0),
                      (1, 1), (1, -1), (-1, 1), (-1, -1)]
        for direction in directions:
            new_i = i + direction[0]
            new_j = j + direction[1]

            if self._check_node_validity((new_i, new_j)) and not self.closed_list[new_i][new_j]:
                if (new_i, new_j) == self.goal:
                    self.found = True
                    self._nodes[new_i][new_j].parent = (i, j)
                    self._nodes[new_i][new_j].g = self._nodes[i][j].g + self._nodes[i][j]. \
                        edges[direction[0] + 1][direction[1] + 1]
                    return self._get_path_to(self.goal)
                else:
                    new_g = self._nodes[i][j].g + self._nodes[i][j]. \
                        edges[direction[0] + 1][direction[1] + 1]
                    new_h = self._heurestic_function((new_i, new_j))
                    new_f = new_g + new_h
                    if self._nodes[new_i][new_j].f == float('inf') or self._nodes[new_i][new_j].f > new_f:
                        heapq.heappush(self.open_list,
                                       (new_f, (new_i, new_j), self._nodes[new_i][new_j]))

                        self._nodes[new_i][new_j].f = new_f
                        self._nodes[new_i][new_j].g = new_g
                        self._nodes[new_i][new_j].h = new_h
                        self._nodes[new_i][new_j].parent = (i, j)

        return False

    def get_path(self):
        '''
        Solves the algorithm and returns path.
        '''
        solved = False
        while not solved:
            solved = self.step()
        return solved

    def _heurestic_function(self, cord: tuple):
        '''
        Gives an estimate of cost from a point to the goal.
        '''
        x_diff = self.goal[0] - cord[0]
        y_diff = self.goal[1] - cord[1]
        z_diff = self._grid[self.goal[0]][self.goal[1]] - \
            self._grid[cord[0]][cord[1]]

        return sqrt(x_diff**2+y_diff**2+z_diff**2)

    def _check_node_validity(self, cord: tuple):
        '''
        Check if a given cordinates are inside the grid.
        '''
        size = len(self._nodes)
        return 0 <= cord[0] < size and 0 <= cord[1] < size

    def _get_path_to(self, cord: tuple):
        '''
        Given cordinates gets the path to those cordinates from the start. 
        Doesn't run the algo. Just gets the path if it alredy exists.
        '''
        path = []
        parent = cord
        while parent != (0, 0):
            if parent in path:
                return path
            path.append(parent)
            parent = self._nodes[parent[0]][parent[1]].parent
