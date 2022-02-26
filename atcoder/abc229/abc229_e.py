import sys

readline = sys.stdin.readline
readline2 = lambda: [int(v) for v in readline().split()]


class UnionFind:
    ROOT = -1

    def __init__(self, n: int):
        self.parent = [self.ROOT] * n
        self.size = [1] * n

    def get_root(self, x: int) -> int:
        hist = []
        while self.parent[x] != self.ROOT:
            hist.append(x)
            x = self.parent[x]
        for y in hist:
            self.parent[y] = x
        return x

    def unite(self, x: int, y: int):
        rx, ry = self.get_root(x), self.get_root(y)
        if rx == ry:
            return
        if self.size[ry] > self.size[rx]:
            rx, ry = ry, rx
        self.parent[ry] = rx
        self.size[rx] += self.size[ry]


N, M = readline2()
G = [[] for _ in range(N)]

for _ in range(M):
    a, b = readline2()
    G[a - 1].append(b - 1)
    G[b - 1].append(a - 1)

uf = UnionFind(N)
ans = [0]

# 大きい頂点からつないでいく
for i in range(N - 1, 0, -1):
    root_set = set()
    for j in G[i]:
        if j < i:
            continue
        root_set.add(uf.get_root(j))
        uf.unite(i, j)
    ans.append(ans[-1] + 1 - len(root_set))

for v in reversed(ans):
    print(v)