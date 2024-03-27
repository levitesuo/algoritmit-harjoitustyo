
class LinkedList:
    def __init__(self, size, start: tuple):
        self._size = size
        self.l = [[None, None] for _ in range((size+1) ** 2)]
        start_list_cord = self._t_to_l(start)

        self.l[start_list_cord] = [size**2, None]
        self.l[size**2][1] = start_list_cord

        self.i = start_list_cord

    def __str__(self):
        l = []
        i = self._size ** 2
        while True:
            i = self.l[i][1]
            if i is None:
                return str(l)
            l.append(self._l_to_t(i))

    def insert_after(self, next: tuple):
        next_cord = self._t_to_l(next)
        if self.l[self.i][1] is not None:
            self.l[self.l[self.i][1]][0] = next_cord
        self.l[next_cord] = [self.i, self.l[self.i][1]]
        self.l[self.i][1] = next_cord

    def delete_if_able(self, cord: tuple):
        delat = self._t_to_l(cord)
        if self.l[delat] == [None, None]:
            return
        self.l[self.l[delat][0]][1] = self.l[delat][1]
        if self.l[delat][1] is not None:
            self.l[self.l[delat][1]][0] = self.l[delat][0]
        self.l[delat] = [None, None]

    def delete_current(self):
        self.l[self.l[self.i][0]][1] = self.l[self.i][1]
        if self.l[self.i][1] is not None and self.l[self.l[self.i][1]] is not None:
            self.l[self.l[self.i][1]][0] = self.l[self.i][0]
        self.l[self.i][0] = None

    def iterate(self):
        if self.l[self.i][1] is None:
            return False
        self.i = self.l[self.i][1]
        return True

    def get_i(self):
        return self._l_to_t(self.i)

    def empty(self):
        return self.l[self._size**2][1] is None

    def _t_to_l(self, t):
        return t[0] * self._size + t[1]

    def _l_to_t(self, i):
        return (i//self._size, i % self._size)
