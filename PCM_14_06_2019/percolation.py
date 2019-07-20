from weightedquickunion import WeightedQuickUnion
import numpy

class Percolation:
    def __init__(self, L):
        self.L = L
        self.sites = numpy.zeros((L, L), dtype = bool)

        self.uf = WeightedQuickUnion(L * L +2)

        self.top = L * L
        self.bottom = L * L + 1

        self.opened = 0

    def getIndex(self, i, j):
        return i * self.L + j 

        # Devuelve el índice
        # En caso contrario: índice // L = i e índice % L = j

    def isOpen(self, i, j):
        return self.sites[i, j] 

        # Devuelve un True o un False dependiendo si el sitio está 
        # abierto o cerrado.

    def open(self, i, j):
        if not self.isOpen(i, j):
            index = self.getIndex(i, j)

            self.sites[i, j] = True

            self.opened += 1

            if (i == 0):
                self.uf.union(index, self.top)

            if (i == self.L - 1):
                self.uf.union(index, self.bottom)

            # UP
            if (i > 0) and self.isOpen(i - 1, j):
                self.uf.union(index, self.getIndex(i - 1, j))

            # BOTTOM
            if (i < (self.L - 1)) and self.isOpen(i + 1, j):
                self.uf.union(index, self.getIndex(i + 1, j))

            # LEFT
            if (j > 0) and self.isOpen(i, j - 1):
                self.uf.union(index, self.getIndex(i, j - 1))

            # RIGHT
            if (j < (self.L - 1)) and self.isOpen(i, j + 1):
                self.uf.union(index, self.getIndex(i, j + 1))

    def percolates(self):
        return self.uf.connected(self.top, self.bottom)

    def numberOfOpenSites(self):
        return self.opened
        


