from heapq import heappush, heappop

split_int_input = lambda: [int(v) for v in input().split()]

N = int(input())
G = [[] for _ in range(N)]
for _ in range(N):
    tmp = split_int_input()
    for v, d in zip(tmp[2::2], tmp[3::2]):
        G[tmp[0]].append((v, d))

ds = [10 ** 15] * N
visited = [False] * N

ds[0] = 0
hq = [(0, 0)]
while len(hq) > 0:
    d, v = heappop(hq)
    if d > ds[v]:
        continue
    for v2, d2 in G[v]:
        d2 += d
        if d2 < ds[v2]:
            heappush(hq, (d2, v2))
            ds[v2] = d2

for i in range(N):
    print(i, ds[i])