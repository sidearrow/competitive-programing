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


H, W = split_int_input()
Q = int(input())

is_red = [False] * (H * W)


uf = UnionFind(H * W)
for _ in range(Q):
    q = split_int_input()
    if q[0] == 1:
        r = q[1] - 1
        c = q[2] - 1
        idx = r * W + c
        is_red[idx] = True
        if idx - W >= 0 and is_red[idx - W]:
            uf.unite(idx, idx - W)
        if idx % W != 0 and is_red[idx - 1]:
            uf.unite(idx, idx - 1)
        if idx % W != (W - 1) and is_red[idx + 1]:
            uf.unite(idx, idx + 1)
        if idx + W < W * H and is_red[idx + W]:
            uf.unite(idx, idx + W)
    else:
        r1, c1, r2, c2 = [v - 1 for v in q[1:]]
        p1 = r1 * W + c1
        p2 = r2 * W + c2
        if is_red[p1] and is_red[p2] and uf.root(p1) == uf.root(p2):
            print("Yes")
        else:
            print("No")
