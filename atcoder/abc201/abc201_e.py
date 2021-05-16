from collections import deque

split_int_input = lambda: [int(v) for v in input().split()]

N = int(input())
G = [[] for _ in range(N + 1)]
for _ in range(N - 1):
    u, v, w = split_int_input()
    G[u].append([v, w])
    G[v].append([u, w])

dist = [0] * (N + 1)
seen = [False] * (N + 1)
dq = deque([[1, 0]])
while len(dq) > 0:
    v, w = dq.popleft()
    dist[v] = w
    for v2, w2 in G[v]:
        if not seen[v2]:
            seen[v2] = True
            dq.append([v2, w ^ w2])

memo = [0] * 61
ans = 0
mod = 10 ** 9 + 7
for i, a in enumerate(dist[1:]):
    tmp = 1
    for j in range(61):
        if a & 1:
            if i > 0:
                ans = (ans + (i - memo[j]) * tmp) % mod
            memo[j] += 1
        else:
            if i > 0:
                ans = (ans + memo[j] * tmp) % mod
        a >>= 1
        tmp = tmp * 2 % mod

print(ans)