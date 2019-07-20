class QuickFind:
    def __init__(self, N):
        self.N = N
        self.id = [i for i in range(N)] #Lista por compresión

    def connected(self, p, q):
        return self.id[p] == self.id[q]

    def union(self, p, q):
        pid = self.id[p]
        qid = self.id[q]

        for i in range(self.N):
            if self.id[i] == pid:
                self.id[i] = qid

        return
