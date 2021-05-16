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


split_int_input = lambda: [int(v) for v in input().split()]

N, K = split_int_input()
A = [split_int_input() for _ in range(N)]
ufa = UnionFind(N)
ufb = UnionFind(N)

for i in range(N):
    for j in range(i + 1, N):
        valid = True
        for a, b in zip(A[i], A[j]):
            if a + b > K:
                valid = False
                break
        if valid:
            ufa.unite(i, j)

for i in range(N):
    for j in range(i + 1, N):
        valid = True
        for k in range(N):
            if A[k][i] + A[k][j] > K:
                valid = False
                break
        if valid:
            ufb.unite(i, j)

ans = 1
mod = 998244353
for i, v in enumerate(ufa.par):
    if v == -1:
        tmp = 1
        for i in range(ufa.size[i]):
            tmp *= i + 1
        ans = ans * tmp % mod
for i, v in enumerate(ufb.par):
    if v == -1:
        tmp = 1
        for i in range(ufb.size[i]):
            tmp *= i + 1
        ans = ans * tmp % mod

print(ans)