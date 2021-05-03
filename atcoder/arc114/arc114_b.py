N = int(input())
f = [int(v) - 1 for v in input().split()]


class UnionFind:
    def __init__(self, n):
        self.parents = [-1] * n
        self.sizes = [1] * n

    def root(self, i):
        r = self.parents[i]
        if r == -1:
            return i
        self.parents[i] = self.root(r)
        return self.parents[i]

    def unite(self, a, b):
        ra = self.root(a)
        rb = self.root(b)
        if ra == rb:
            return
        if self.sizes[rb] > self.sizes[ra]:
            ra, rb = rb, ra
        self.parents[rb] = ra
        self.sizes[ra] += self.sizes[rb]
        self.sizes[rb] = 0


uf = UnionFind(N)
for i, v in enumerate(f):
    if i != v:
        uf.unite(i, v)

ans = 1
mod = 998244353
for v in uf.parents:
    if v == -1:
        ans *= 2
        ans %= mod
print(ans - 1)