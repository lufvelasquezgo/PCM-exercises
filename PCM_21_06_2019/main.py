from lattice import Lattice
from matplotlib import pyplot
from itertools import product
import numpy

L = 100
p_arr = numpy.linspace(0, 1, 200)
num_clusters = []

for p in p_arr:
	sites = list(product(range(L), repeat=2))
	numpy.random.shuffle(sites)
	N = int(p * L * L)

	lattice = Lattice(L)

	for site in sites[:N]:
		lattice.open(*site) # * desacopla la tupla

	sites = list(product(range(L), repeat=2))
	roots = [lattice.uf.root(lattice.getIndex(*site)) for site in sites]
	roots = numpy.array(roots)

	roots = roots.reshape(L, L)
	roots[lattice.sites == False] = -1

	set_roots = set(roots.flatten())
	set_roots = set_roots - {-1}

	num_clusters.append(len(set_roots))

pyplot.figure()
pyplot.plot(p_arr, num_clusters, '*', ms=5, color='magenta')
pyplot.xlabel('Site ocupation probability')
pyplot.ylabel('Number of clusters')
pyplot.grid()
pyplot.tight_layout()
pyplot.savefig('probability.pdf')
pyplot.close()
