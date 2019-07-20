from percolation import Percolation
import numpy
from itertools import product
from plot import plot_lattice

def main():
    L = 20
    trials = 15
    values = []

    for _ in range(trials):
        lattice = Percolation(L)
        sites = list(product(range(L), repeat = 2))
        numpy.random.shuffle(sites)

        while not lattice.percolates():
            i, j = sites[0]
            sites.remove(sites[0])
            lattice.open(i, j)
            plot_lattice(lattice, labels = True)

    print(lattice.numberOfOpenSites() / L * L)

if __name__ == '__main__':
    main()