from math import sqrt
from algorithms.a_star import a_star


class TestNode:
    def __init__(self, position, grid):
        self.position = position
        self.height = 0
        self.parent = None
        self.edges = []

        self.f = float('inf')
        self.g = float('inf')
        self.h = 0

        self._init_edges(grid)

    def _init_edges(self, grid):
        x = self.position[0]
        y = self.position[1]
        cardinal_directions = [(1, 0), (0, -1), (-1, 0), (0, 1)]
        cardinal_accessable = [False, False, False, False]
        for i, direction in enumerate(cardinal_directions):
            new_x = direction[0] + x
            new_y = direction[1] + y
            # print(f"g[0]:{len(grid[0])}\tg:{len(grid)}\tx: {new_x}\ty: {new_y}")
            if len(grid[0]) > new_x > 0 and len(grid) > new_y > 0 and grid[new_y][new_x] == ".":
                cardinal_accessable[i] = True
                self.edges.append((1, new_x * len(grid) + new_y))
        for i in range(4):
            if cardinal_accessable[i] and cardinal_accessable[i-1]:
                direction = (cardinal_directions[i][0]+cardinal_directions[i-1]
                             [0], cardinal_directions[i][1]+cardinal_directions[i-1][1])
                new_x = direction[0] + x
                new_y = direction[1] + y
                self.edges.append(
                    (1.41421356, new_x * len(grid) + new_y))
        self.edges = sorted(self.edges)


def test_heurestics(a, cord, goal):
    size = int(sqrt(len(a)))
    x_diff = cord // size - goal // size
    y_diff = cord % size - goal % size
    return sqrt(x_diff**2 + y_diff**2)


def map_file_translator(start, goal, grid, algorithm):
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
    rows.pop()
    for i in range(len(rows)-1):
        for j in range(len(rows[i])):
            nodes.append(TestNode((j, i), rows))
    transformed_start = start[0] * len(rows) + start[1]
    transformed_goal = goal[0] * len(rows) + goal[1]
    result = algorithm(start=transformed_start,
                       goal=transformed_goal,
                       node_list=nodes,
                       heurestic_function=test_heurestics
                       )
    return result


if __name__ == "__main__":
    with open("/home/leevisuo/Code/algoritmit-harjiotusty-/src/tests/maps/AR0020SR.map", "r") as f:
        print(map_file_translator((65, 24), (48, 43), f.read(), a_star))
    # 65	24	48	43	26.04163055
