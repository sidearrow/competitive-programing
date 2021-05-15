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
N, M, K = split_int_input()
FR = [[] for _ in range(N)]
BR = [[] for _ in range(N)]
st = UnionFind(N)
for _ in range(M):
    a, b = split_int_input()
    st.unite(a - 1, b - 1)
    FR[a - 1].append(b - 1)
    FR[b - 1].append(a - 1)
for _ in range(K):
    c, d = split_int_input()
    BR[c - 1].append(d - 1)
    BR[d - 1].append(c - 1)
ans = []
for i in range(N):
    r = st.root(i)
    tmp = st.size[r] - 1
    for br in BR[i]:
        if r == st.root(br):
            tmp -= 1
    for fr in FR[i]:
        if r == st.root(fr):
            tmp -= 1
    ans.append(tmp)

print(*ans)