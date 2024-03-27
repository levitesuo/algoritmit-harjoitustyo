from math import sqrt
from node import Node
from high_map_func import height_mapping_function
from doubly_linked_list import LinkedList


class FringeSearch:
    def __init__(self):
        self.cache = []
        self.wlist = None
        self._nodes = []
        self.goal = None
        self._grid = None

    def get_path(self, start, goal, grid):
        self.goal = goal
        self._grid = grid
        size = len(grid)
        self._nodes = [[Node((i, j), grid, height_mapping_function)
                        for i in range(size)] for j in range(size)]
        self.cache = [[None for _ in range(size)] for _ in range(size)]
        self.wlist = LinkedList(size, start)
        self.cache[start[0]][start[1]] = (0, (-1, -1))

        found = False
        f_limit = self._heurestic_function(start)
        while not found:
            self.wlist.i = size**2
            f_min = float('inf')
            while True:
                if not self.wlist.iterate():
                    break
                n = self.wlist.get_i()
                g, _ = self.cache[n[0]][n[1]]
                f = g + self._heurestic_function(n)
                if f > f_limit:
                    f_min = min(f, f_min)
                    break
                if n == self.goal:
                    found = True
                    print(g)
                    self._nodes[self.goal[0]][self.goal[1]].g = g
                    break
                for j in range(len(self._nodes[n[0]][n[1]].fedges)-1, -1, -1):
                    s = self._nodes[n[0]][n[1]].fedges[j]
                    s_x, s_y = s[1]
                    g_s = g + s[0]
                    if self.cache[s_x][s_y]:
                        g_o, _ = self.cache[s_x][s_y]
                        if g_s >= g_o:
                            continue
                    self.wlist.delete_if_able((s_x, s_y))
                    self.wlist.insert_after((s_x, s_y))
                    print(self.wlist)
                    self.cache[s_x][s_y] = (g_s, n)
                    self._nodes[n[0]][n[1]].g = g_s
                self.wlist.delete_current()
            f_limit = f_min
        if found:
            return self._get_path()

    def _heurestic_function(self, cord: tuple):
        '''
        Gives an estimate of cost from a point to the goal.
        '''
        x_diff = self.goal[0] - cord[0]
        y_diff = self.goal[1] - cord[1]
        z_diff = self._grid[self.goal[0]][self.goal[1]] - \
            self._grid[cord[0]][cord[1]]

        return sqrt(x_diff**2+y_diff**2+z_diff**2)

    def _get_path(self):
        path = []
        g, parent = self.cache[self.goal[0]][self.goal[1]]
        while parent != (-1, -1):
            path.append(parent)
            g, new_parent = self.cache[parent[0]][parent[1]]
            parent = new_parent
        c = path[0]
        print(self.goal[0]-c[0], self.goal[1]-c[1])
        print(self._nodes[c[0]][c[1]].g)

        return path
