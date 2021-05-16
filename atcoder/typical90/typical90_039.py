from collections import deque

split_int_input = lambda: [int(v) for v in input().split()]

N = int(input())
G = [[] for _ in range(N + 1)]

for _ in range(N - 1):
    a, b = split_int_input()
    G[a].append(b)
    G[b].append(a)

memo = [0] * (N + 1)
dq = deque([1])
seen = [False] * (N + 1)
seen[1] = True
while len(dq) > 0:
    v = dq[-1]
    all_seen = True
    for v2 in G[v]:
        if not seen[v2]:
            seen[v2] = True
            dq.append(v2)
            all_seen = False
    if all_seen:
        v = dq.pop()
        memo[v] = 1 + sum(memo[v2] for v2 in G[v])

ans = 0
for v in memo[1:]:
    ans += v * (N - v)
print(ans)
