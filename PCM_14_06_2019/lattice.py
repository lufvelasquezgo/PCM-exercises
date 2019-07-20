from .WeightedQuickUnion import WeightedQuickUnion
import numpy


class Lattice:
    def __init__(self, L):
        self.L = L
        self.sites = numpy.zeros((L, L), dtype=bool)
        self.opened = 0

        self.uf = WeightedQuickUnion(L * L)


    def getIndex(self, i, j):
        return j * self.L + i


    def isOpen(self, i, j):
        return self.sites[i, j]


    def open(self, i, j):
        if not self.sites[i, j]:
            index = self.getIndex(i, j)

            self.opened += 1

            self.sites[i, j] = True

            # left
            if (j > 0) and self.isOpen(i, j - 1):
                self.uf.union(index, self.getIndex(i, j - 1))

            # right
            if (j < (self.L - 1)) and self.isOpen(i, j + 1):
                self.uf.union(index, self.getIndex(i, j + 1))

            # up
            if (i > 0) and self.isOpen(i - 1, j):
                self.uf.union(index, self.getIndex(i - 1, j))

            # down
            if (i < (self.L - 1)) and self.isOpen(i + 1, j):
                self.uf.union(index, self.getIndex(i + 1, j))


    def numberOfOpenSites(self):
        return self.opened


    def clusters(self):
        roots = numpy.zeros((self.L, self.L), dtype=int)

        for i in range(self.L):
            for j in range(self.L):
                roots[i, j] = self.uf.root(self.getIndex(i, j))

        roots[self.sites == False] = -1

        set_roots = sorted(set(roots.flatten()))[1:]
        for i, id in enumerate(set_roots):
            roots[roots == id] = i + 1

        roots[self.sites == False] = 0

        return roots, len(set_roots)
