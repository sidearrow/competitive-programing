import sys

sys.setrecursionlimit(10 ** 7)

split_int_input = lambda: [int(v) for v in input().split()]


class WeightedUnionFind:
    def __init__(self, n):
        self.parent = [-1] * n
        self.diff_weight = [-1] * n
        self.size = [1] * n

    def root(self, x):
        if self.parent[x] == -1:
            return x
        r = self.root(self.parent[x])
        self.diff_weight[x] += self.diff_weight[self.parent[x]]
        self.parent[x] = r
        return r

    def weight(self, x):
        self.root(x)
        return self.diff_weight[x]

    def unite(self, a, b, w):
        w += self.weight(a)
        w -= self.weight(b)
        a = self.root(a)
        b = self.root(b)
        if a == b:
            return
        if self.size[a] < self.size[b]:
            a, b = b = a
            w = -w
        self.parent[b] = a
        self.diff_weight[b] = w

    def diff(self, x, y):
        return self.weight(y) - self.weight(x)


N, Q = split_int_input()
queries = [split_int_input() for _ in range(Q)]

wuf = WeightedUnionFind(N)
for q in queries:
    if q[0] == 0:
        wuf.unite(q[1], q[2], q[3])
        continue
    d = wuf.diff(q[1], q[2])
    if d is None:
        print("?")
    else:
        print(d)