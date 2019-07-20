from matplotlib import pyplot
from matplotlib.patches import Rectangle
from itertools import product

def plot_lattice(lattice,
    labels=False,
    coordinates=False, colors={"open":"lightblue", "closed":"blue", "top":"pink"}):
    fig = pyplot.figure(figsize=(lattice.L, lattice.L))
    ax = fig.add_subplot(111)
    for i, j in product(range(lattice.L), repeat=2):
        if lattice.sites[i, j]:
            color = colors["open"]
            if lattice.connectedToTop(i, j):
                color = colors["top"]
        else:
            color = colors["closed"]

        x = i
        y = lattice.L - j - 1
        sq = Rectangle((x + 0.05, y + 0.05), 0.9, 0.9, facecolor=color, edgecolor="black", lw=2)
        if labels:
            if coordinates:
                ax.text(x + 0.5, y + 0.5, str(lattice.getIndex(i, j)) + "\n" + str((i, j)), va="center", ha="center", fontsize=16)
            else:
                ax.text(x + 0.5, y + 0.5, lattice.getIndex(i, j), va="center", ha="center", fontsize=16)

        ax.add_patch(sq)

    ax.set_xticks([])
    ax.set_yticks([])
    ax.set_xlim(0, lattice.L)
    ax.set_ylim(0, lattice.L)
    ax.set_aspect("equal")
    pyplot.axis('off')
    pyplot.tight_layout()
    pyplot.savefig("lattice.pdf")
    pyplot.close()