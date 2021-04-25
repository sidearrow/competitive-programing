from heapq import *

split_int_input = lambda: [int(v) for v in input().split()]

VL, EL, R = split_int_input()
G = [[] for _ in range(VL)]
for _ in range(EL):
    s, t, d = split_int_input()
    G[s].append([t, d])

ans = [10 ** 15] * VL
ans[R] = 0
hq = [[0, R]]
seen = [False] * VL

while len(hq) > 0:
    d, v = heappop(hq)
    if d > ans[v]:
        continue
    for v2, d2 in G[v]:
        d2 += d
        if d2 < ans[v2]:
            ans[v2] = d2
            heappush(hq, [d2, v2])

for v in ans:
    if v == 10 ** 15:
        print("INF")
    else:
        print(v)