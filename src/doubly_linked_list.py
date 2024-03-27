class LinkedList:
    def __init__(self, size, start: tuple):
        self._size = size
        self.l = [{'past': None, 'next': None} for _ in range((size+1) ** 2)]
        start_list_cord = self._t_to_l(start)

        self.l[start_list_cord] = {
            'past': size**2, 'next': None}
        self.l[size**2]['next'] = start_list_cord

        self.i = start_list_cord

    def __str__(self):
        l = []
        i = self._size ** 2
        while True:
            i = self.l[i]['next']
            if i is None:
                return str(l)
            l.append(self._l_to_t(i))

    def insert_after(self, next: tuple):
        next_cord = self._t_to_l(next)
        self.l[next_cord] = {'past': self.i, 'next': self.l[self.i]['next']}
        self.l[self.i]['next'] = next_cord

    def delete_if_able(self, cord: tuple):
        delat = self._t_to_l(cord)
        if self.l[delat] == {'past': None, 'next': None}:
            return
        print(self)
        print(self._l_to_t(self.i))
        if self.l[self.l[delat]['past']] is not None:
            self.l[self.l[delat]['past']]['next'] = self.l[delat]['next']
        if self.l[self.l[self.i]['next']] is not None:
            self.l[self.l[delat]['next']]['past'] = self.l[delat]['past']
        self.l[delat] = {'past': None, 'next': None}

    def delete_current(self):
        self.l[self.l[self.i]['past']]['next'] = self.l[self.i]['next']
        if self.l[self.l[self.i]['next']] is not None:
            self.l[self.l[self.i]['next']]['past'] = self.l[self.i]['past']
        self.l[self.i]['past'] = None

    def iterate(self):
        if self.l[self.i]['next'] is None:
            return False
        self.i = self.l[self.i]['next']
        return True

    def get_i(self):
        return self._l_to_t(self.i)

    def _t_to_l(self, t):
        return t[0] * self._size + t[1]

    def _l_to_t(self, i):
        return (i//self._size, i % self._size)
