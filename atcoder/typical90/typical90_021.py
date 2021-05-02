import sys

sys.setrecursionlimit(10 ** 7)

split_int_input = lambda: [int(v) for v in input().split()]

N, M = split_int_input()
G1 = [[] for _ in range(N)]
G2 = [[] for _ in range(N)]
for _ in range(M):
    a, b = split_int_input()
    a, b = a - 1, b - 1
    G1[a].append(b)
    G2[b].append(a)


class DFS1:
    def __init__(self):
        self.seen = [False] * N
        self.result = []

    def search(self, v):
        self.seen[v] = True
        for v2 in G1[v]:
            if not self.seen[v2]:
                self.search(v2)
        self.result.append(v)

    def exec(self):
        for v in range(N):
            if not self.seen[v]:
                self.search(v)


class DFS2:
    def __init__(self):
        self.seen = [False] * N
        self.res = 0
        self.cnt = 0

    def search(self, v):
        self.seen[v] = True
        self.cnt += 1
        for v2 in G2[v]:
            if not self.seen[v2]:
                self.search(v2)

    def exec(self, vs):
        for v in vs:
            self.cnt = 0
            if not self.seen[v]:
                self.search(v)
                self.res += self.cnt * (self.cnt - 1) // 2


dfs1 = DFS1()
dfs1.exec()

dfs2 = DFS2()
dfs2.exec(reversed(dfs1.result))

print(dfs2.res)