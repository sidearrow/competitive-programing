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
        self.par[ry] = rx
        self.size[rx] += self.size[ry]


N, M = split_int_input()
P = split_int_input()

uf = UnionFind(N)
for _ in range(M):
    x, y = split_int_input()
    uf.unite(x - 1, y - 1)

ans = 0
for i, v in enumerate(P):
    if uf.root(i) == uf.root(v - 1):
        ans += 1

print(ans)
