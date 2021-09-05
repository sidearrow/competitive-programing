from bisect import bisect_left


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

L, Q = split_int_input()

CX = []
breaks = []
# 長さを出力
b = []
for _ in range(Q):
    c, x = split_int_input()
    CX.append([c, x])
    if c == 1:
        breaks.append(x)
    else:
        b.append(x)
CX = list(reversed(CX))

# 長さ
fragments = []
tmp = 0
breaks = sorted(breaks)
breaks_idx = {}
for i, v in enumerate(breaks):
    breaks_idx[v] = i
    fragments.append(v - tmp)
    tmp = v
fragments.append(L - tmp)

d = {}
for v in b:
    d[v] = bisect_left(breaks, v)

uf = UnionFind(len(fragments))
uf.size = fragments

ans = []
for c, x in CX:
    if c == 1:
        uf.unite(breaks_idx[x], breaks_idx[x] + 1)
    else:
        tmp = uf.size[uf.get_root(d[x])]
        ans.append(tmp)

print(*reversed(ans), sep="\n")