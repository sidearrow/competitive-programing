class UnionFind:
    def __init__(self, n):
        self.par = [-1] * n
        self.size = [1] * n

    def get_root(self, x):
        if self.par[x] == -1:
            return x
        self.par[x] = self.get_root(self.par[x])
        return self.par[x]

    def unite(self, x, y):
        rx, ry = self.get_root(x), self.get_root(y)
        if rx == ry:
            return
        if self.size[ry] > self.size[rx]:
            rx, ry = ry, rx
        self.par[ry] = rx
        self.size[rx] += self.size[ry]


split_int_input = lambda: [int(v) for v in input().split()]

V, E = split_int_input()
edges = [split_int_input() for _ in range(E)]
edges.sort(key=lambda v: v[2])

uf = UnionFind(V)
ans = 0
for s, t, w in edges:
    if uf.get_root(s) == uf.get_root(t):
        continue
    ans += w
    uf.unite(s, t)

print(ans)