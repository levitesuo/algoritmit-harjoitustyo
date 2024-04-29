from math import sqrt


class LinkedList:
    '''
    An implementation of a doubly linked list outlined in this paper https://webdocs.cs.ualberta.ca/~holte/Publications/fringe.pdf
    Has a default starting node at [size]
    '''

    def __init__(self, size, start):
        self._size = size
        self.l = [[None, None] for _ in range(size + 1)]

        self.l[start] = [size, None]
        self.l[size][1] = start

        self.i = start

    def __str__(self):
        return str(self.get_list())

    def get_list(self):
        '''
        Transforms the linked list to a conventional list and returns it.
        Also performs a transformation of cordinates where the assumption is made that the original map is  a square.
        '''
        l = []
        i = self._size
        while True:
            i = self.l[i][1]
            if i is None:
                return l
            l.append(i)

    def insert_after(self, next):
        '''
        Inserts given cell after the current cell.
        '''
        if self.l[self.i][1] is not None:
            self.l[self.l[self.i][1]][0] = next
        self.l[next] = [self.i, self.l[self.i][1]]
        self.l[self.i][1] = next

    def delete_if_able(self, cord):
        '''
        Deletes a cell if it exists.
        '''
        if self.l[cord] == [None, None]:
            return
        if self.l[cord][0] is not None:
            self.l[self.l[cord][0]][1] = self.l[cord][1]
        if self.l[cord][1] is not None:
            self.l[self.l[cord][1]][0] = self.l[cord][0]
        self.l[cord] = [None, None]

    def delete_current(self):
        '''
        Deletes the cell that the iteration is currently on.
        '''
        # Sets i:s previouses next to i:s next

        self.l[self.l[self.i][0]][1] = self.l[self.i][1]
        if self.l[self.i][1] is not None and self.l[self.l[self.i][1]] is not None:
            self.l[self.l[self.i][1]][0] = self.l[self.i][0]
        self.l[self.i][0] = None

    def iterate(self):
        '''
        Iterates the list one step further.
        '''
        if self.l[self.i][1] is None:
            return False
        self.i = self.l[self.i][1]
        return True

    def get_i(self):
        '''
        Returns the current iteration
        '''
        return self.i

    def empty(self):
        '''
        Return bool that tells if the list is empty.
        '''
        # If the default starting node is pointing to empty. The list has nothing in it.
        return self.l[self._size][1] is None
