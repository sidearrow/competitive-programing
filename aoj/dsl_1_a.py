import sys

sys.setrecursionlimit(10 ** 7)

split_int_input = lambda: [int(v) for v in input().split()]


class UnionFind:
    def __init__(self, n):
        self.par = [-1] * n
        self.size = [1] * n

    def root(self, x):
        par = self.par[x]
        if par == -1:
            return x
        self.par[x] = self.root(par)
        return self.par[x]

    def unite(self, x, y):
        rx = self.root(x)
        ry = self.root(y)
        if rx == ry:
            return
        if self.size[ry] > self.size[rx]:
            rx, ry = ry, rx
        self.par[rx] = ry
        self.size[rx] += self.size[ry]

    def is_same(self, x, y):
        rx = self.root(x)
        ry = self.root(y)
        return rx == ry


N, Q = split_int_input()
COM = [split_int_input() for _ in range(Q)]

uf = UnionFind(N)
for c in COM:
    com = c[0]
    x = c[1]
    y = c[2]
    if com == 1:
        print(int(uf.is_same(x, y)))
    else:
        uf.unite(x, y)
