class UnionFind:
    def __init__(self, n):
        self.root = [-1] * n
        self.size = [1] * n

    def get_root(self, x):
        if self.root[x] == -1:
            return x
        self.root[x] = self.get_root(self.root[x])
        return self.root[x]

    def unite(self, x, y):
        rx, ry = self.get_root(x), self.get_root(y)
        if rx == ry:
            return
        if self.size[ry] > self.size[rx]:
            rx, ry = ry, rx
        self.root[ry] = rx
        self.size[rx] += self.size[ry]


split_int_input = lambda: [int(v) for v in input().split()]

N, M = split_int_input()
uf = UnionFind(N)
for _ in range(M):
    x, y, z = split_int_input()
    uf.unite(x - 1, y - 1)

ans = 0
for r in uf.root:
    if r == -1:
        ans += 1

print(ans)