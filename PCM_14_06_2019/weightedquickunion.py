class WeightedQuickUnion:
    def __init__(self, N):
        self.N = N
        self.parent = [i for i in range(N)]
        self.rank = [0 for i in range(N)] # o se puede utilizar "[0] * N"

    def root(self, i):
        while (i != self.parent[i]):
            i = self.parent[i]
        return i 

    def connected(self, p, q):
        return self.root(p) == self.root(q)

    def union(self, p, q):
        proot = self.root(p)
        qroot = self.root(q)

        if self.rank[proot] < self.rank[qroot]:
            self.parent[proot] = qroot
        elif self.rank[qroot] < self.rank[proot]:
            self.parent[qroot] = proot
        else:
            self.parent[proot] = qroot
            self.rank[qroot] += 1