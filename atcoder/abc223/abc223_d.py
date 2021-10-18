import sys
from heapq import heappush, heappop

readline = sys.stdin.readline
readline2 = lambda: [int(v) for v in readline().split()]

N, M = readline2()
G = [[] for _ in range(N + 1)]
memo = [0] * N
for _ in range(M):
    a, b = readline2()
    G[a - 1].append(b - 1)
    memo[b - 1] += 1

q = []
for i, v in enumerate(memo):
    if v == 0:
        q.append(i)

ans = []
while len(q) > 0:
    v = heappop(q)
    ans.append(v + 1)
    for v2 in G[v]:
        memo[v2] -= 1
        if memo[v2] == 0:
            heappush(q, v2)

if len(ans) == N:
    print(*ans)
else:
    print(-1)