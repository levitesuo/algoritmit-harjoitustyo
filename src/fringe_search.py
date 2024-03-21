from math import sqrt
from node import Node
from high_map_func import height_mapping_function


class FringeSearch:
    def __init__(self):
        self.cache = []
        self.wlist = []
        self._nodes = []
        self._removed_nodes = []
        self.f_limit = 0
        self.goal = None
        self._grid = None
# Lista jossa pidetään kirjaa jokaisesta nodesta.
# Nodella voi olla kolme tilaa
# 0. Not seen
# 1. Read once the remove
# 2. Remove if seen

# Kaikki nodet aloittavat samasta tilasta 1 ja kun ne nähdään siirretään ne tilaan 2.
# Kun node on luettu se siirretään tilan kolme ja jos sitä yritettään lukea uudestaan se poistetaan.
# Jos node on tilassa 3 ja se nähdään se siirtyy tilaan 2

    def init(self, start, goal, grid):
        self.goal = goal
        self._grid = grid
        size = len(grid)
        self._nodes = [[Node((i, j), grid, height_mapping_function)
                        for i in range(size)] for j in range(size)]

        self.wlist.append(start)

        for i in range(size):
            self.cache.append([])
            self._removed_nodes.append([])
            for j in range(size):
                self.cache[i].append(None)
                self._removed_nodes[i].append(0)

        self.cache[start[0]][start[1]] = (0, (-1, -1))
        self.f_limit = self._heurestic_function(start)

    def get_path(self):
        found = False
        while not found and len(self.wlist) > 0:
            f_min = float('inf')
            i = -1
            while i < len(self.wlist) - 1:
                i += 1
                n = self.wlist[i]
                g, parent = self.cache[n[0]][n[1]]
                f = g + self._heurestic_function(n)
                if f > self.f_limit:
                    f_min = min(f, f_min)
                    continue
                if n == self.goal:
                    found = True
                    break
                for j in range(len(self._nodes[n[0]][n[1]].fedges)-1, -1, -1):
                    s = self._nodes[n[0]][n[1]].fedges[j]
                    s_x, s_y = s[1]
                    g_s = g + s[0]
                    if self.cache[s_x][s_y]:
                        g_o, _ = self.cache[s_x][s_y]
                        if g_s >= g_o:
                            continue
                    if (s_x, s_y) in self.wlist:
                        self.wlist.remove((s_x, s_y))
                    self.wlist = self.wlist[0:i] + \
                        [(s_x, s_y)] + self.wlist[i:]
                    self.cache[s_x][s_y] = (g_s, n)
                self.wlist.remove(n)
                i -= 1
            self.f_limit = f_min
        if found:
            print("Fringe Search found a path")
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
        print(g)
        while parent != (-1, -1):
            path.append(parent)
            g, new_parent = self.cache[parent[0]][parent[1]]
            parent = new_parent

        return path
