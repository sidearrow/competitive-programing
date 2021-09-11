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

N = int(input())
UVW = [split_int_input() for _ in range(N - 1)]
UVW = sorted(UVW, key=lambda v: v[2])

ans = 0
uf = UnionFind(N)
for u, v, w in UVW:
    size_a = uf.size[uf.get_root(u - 1)]
    size_b = uf.size[uf.get_root(v - 1)]
    ans += w * size_a * size_b
    uf.unite(u - 1, v - 1)

print(ans)
