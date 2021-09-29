import sys
from collections import deque

readline = sys.stdin.readline
readline_split_int = lambda: [int(v) for v in readline().split()]

N = int(readline())
G = [[] for _ in range(N)]
E = []
for _ in range(N - 1):
    a, b = readline_split_int()
    E.append([a - 1, b - 1])
    G[a - 1].append(b - 1)
    G[b - 1].append(a - 1)
Q = int(readline())
TEX = [readline_split_int() for _ in range(Q)]

depth = [-1] * N
depth[0] = 0
dq = deque()
dq.append(0)
while len(dq) > 0:
    v1 = dq.pop()
    for v2 in G[v1]:
        if depth[v2] == -1:
            depth[v2] = depth[v1] + 1
            dq.append(v2)

memo = [0] * N
for t, e, x in TEX:
    a, b = E[e - 1]
    da, db = depth[a], depth[b]
    if t == 1:
        if da < db:
            memo[0] += x
            memo[b] -= x
        else:
            memo[a] += x
    else:
        if da < db:
            memo[b] += x
        else:
            memo[0] += x
            memo[a] -= x

seen = [False] * N
seen[0] = True
dq = deque()
dq.append(0)
while len(dq) > 0:
    v1 = dq.pop()
    for v2 in G[v1]:
        if not seen[v2]:
            memo[v2] += memo[v1]
            seen[v2] = True
            dq.append(v2)

for v in memo:
    print(v)