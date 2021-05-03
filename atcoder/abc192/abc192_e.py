import math
from heapq import heappush, heappop

split_int_input = lambda: [int(v) for v in input().split()]

N, M, X, Y = split_int_input()
G = [[] for _ in range(N + 1)]
for _ in range(M):
    a, b, t, k = split_int_input()
    G[a].append((b, t, k))
    G[b].append((a, t, k))

ds = [10 ** 15] * (N + 1)
ds[X] = 0
hq = [(0, X)]
while len(hq) > 0:
    d, v = heappop(hq)
    if d > ds[v]:
        continue
    for v2, t, k in G[v]:
        d2 = math.ceil(d / k) * k + t
        if d2 < ds[v2]:
            heappush(hq, (d2, v2))
            ds[v2] = d2

if ds[Y] == 10 ** 15:
    print(-1)
else:
    print(ds[Y])