# Tämä koodi on kirjoitettu sivun https://www.geeksforgeeks.org/a-search-algorithm/ pohjalta.
# Joka ikinen merkki on kuitenkin kirjoitettu itse.

class Cell:
    def __init__(self):
        self.parent_i = 0
        self.parent_j = 0
        self.f = float('int')
        self.g = float('inf')
        self.h = 0
