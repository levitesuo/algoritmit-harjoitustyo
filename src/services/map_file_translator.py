from math import sqrt
from algorithms.a_star import a_star
from copy import copy


class TestNode:
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
                self.edges.append((1.41421356237, dia_x * len(grid) + dia_y))
                g[dia_y][dia_x] = "D"


def test_heurestics(a, cord, goal):
    '''
    Heurestics function for .map files.
    Assumes the size of the grid is a square.
    '''
    size = int(sqrt(len(a)))
    x_diff = cord // size - goal // size
    y_diff = cord % size - goal % size
    return sqrt(x_diff**2 + y_diff**2)


def map_file_translator(start, goal, grid, algorithm, heurestic=test_heurestics):
    '''
    A function that translates .map files to a readable format for the algorithms.
    Then translates the result back to cordinates.
    This method is intended for usage in testing so it also rips all the other data from the algorithms outpus and returns only translated path.

    Parameters:
        grid (str): The content of .map file
        start and goal (tuples): tuples of cordinates corresponding to the start and the goal of path.
        algorithm (function): A function that takes inputs start, goal and node_map.

    Returns:
        path (list): A list of tuples / cordinates corresponding to the shortest path.
    '''
    nodes = []
    rows = grid.split("\n")[4:]
    print(rows)
    rows.pop()
    for i in range(len(rows)):
        for j in range(len(rows)):
            nodes.append(TestNode((i, j), rows))
    transformed_start = start[0] * len(rows) + start[1]
    transformed_goal = goal[0] * len(rows) + goal[1]
    result = algorithm(start=transformed_start,
                       goal=transformed_goal,
                       node_list=nodes,
                       heurestic_function=heurestic
                       )
    return result
