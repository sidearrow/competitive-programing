import sys

sys.setrecursionlimit(10 ** 7)
readline = sys.stdin.readline
readline_split_int = lambda: [int(v) for v in readline().split()]

N = int(readline())
G = [[] for _ in range(N + 1)]
for _ in range(N - 1):
    u, v = readline_split_int()
    G[u].append(v)
    G[v].append(u)

dist = [0] * (N + 1)
child_num = [0] * (N + 1)
seen = [False] * (N + 1)


def dfs1(v, d):
    cn = 0
    for v2 in G[v]:
        if not seen[v2]:
            seen[v2] = True
            cn += dfs1(v2, d + 1)
            cn += 1
    child_num[v] = cn
    dist[v] = d
    return cn


seen[1] = True
dfs1(1, 0)

for i in range(N + 1):
    seen[i] = False

ans = [0] * (N + 1)


def dfs2(v):
    for v2 in G[v]:
        if not seen[v2]:
            seen[v2] = True
            ans[v2] = ans[v] - (child_num[v2] + 1) + (N - child_num[v2] - 1)
            dfs2(v2)


seen[1] = True
ans[1] = sum(dist)
dfs2(1)

for v in ans[1:]:
    print(v)