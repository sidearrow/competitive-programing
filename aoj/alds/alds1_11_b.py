import sys

sys.setrecursionlimit(10 ** 7)
split_int_input = lambda: [int(v) for v in input().split()]

N = int(input())
G = [[] for _ in range(N + 1)]
for _ in range(N):
    tmp = split_int_input()
    if len(tmp) == 2:
        continue
    id = tmp[0]
    for v in tmp[2:]:
        G[id].append(v)

seen = [False] * (N + 1)
d = [0] * (N + 1)
f = [0] * (N + 1)
t = 0


def dfs(v):
    seen[v] = True
    global t
    t += 1
    d[v] = t
    for v2 in G[v]:
        if not seen[v2]:
            dfs(v2)
    t += 1
    f[v] = t


for i in range(1, N + 1):
    if not seen[i]:
        dfs(i)

for i in range(1, N + 1):
    print(i, d[i], f[i])