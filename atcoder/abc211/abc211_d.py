from collections import deque

INF = float("inf")
MOD = 10 ** 9 + 7

split_int_input = lambda: [int(v) for v in input().split()]

N, M = split_int_input()
G = [[] for _ in range(N + 1)]
for _ in range(M):
    a, b = split_int_input()
    G[a].append(b)
    G[b].append(a)

dq = deque([1])
seen = [False] * (N + 1)
n = [0] * (N + 1)
dist = [INF] * (N + 1)
seen[1] = True
n[1] = 1
dist[1] = 0
while len(dq) > 0:
    v = dq.popleft()
    for v2 in G[v]:
        if not seen[v2]:
            dq.append(v2)
            seen[v2] = True
        if dist[v2] > dist[v] + 1:
            dist[v2] = dist[v] + 1
            n[v2] = n[v]
        elif dist[v2] == dist[v] + 1:
            n[v2] = (n[v] + n[v2]) % MOD

print(n[-1])