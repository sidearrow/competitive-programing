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
        self.par[ry] = rx
        self.size[rx] += self.size[ry]

    def is_same(self, x, y):
        rx = self.root(x)
        ry = self.root(y)
        return rx == ry
