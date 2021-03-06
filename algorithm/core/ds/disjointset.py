# AUTOGENERATED! DO NOT EDIT! File to edit: nbs/00_disjoint_set.ipynb (unless otherwise specified).

__all__ = ['DisjointSet']

# Cell

class DisjointSet:
    def __init__(self, s):
        self.parent = {n:n for n in s}

    def find(self, x):
        while x != self.parent[x]:
            self.parent[x] = self.parent[self.parent[x]]
            x = self.parent[x]
        return x

    def union(self, x, y):
        root_x, root_y = self.find(x), self.find(y)
        self.parent[root_y] = root_x

    def is_same(self, x, y):
        return self.find(x) == self.find(y)

    def __repr__(self) -> str:
        """
        Print self in a reproducible way.
        >>> DisjointSet({1: 2, 2: 2})
        DisjointSet({1: 2, 2: 2})
        """
        return f"{self.__class__.__name__}({self.parent})"
