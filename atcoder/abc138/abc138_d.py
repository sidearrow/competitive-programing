from collections import deque

input_split_int = lambda: [int(v) for v in input().split()]

N, Q = input_split_int()
G = [[] for _ in range(N + 1)]
for _ in range(N - 1):
    a, b = input_split_int()
    G[a].append(b)
    G[b].append(a)
cnt = [0] * (N + 1)
for _ in range(Q):
    p, x = input_split_int()
    cnt[p] += x

dq = deque()
dq.append(1)
seen = [False] * (N + 1)
seen[1] = True
while len(dq) > 0:
    v1 = dq.popleft()
    x = cnt[v1]
    for v2 in G[v1]:
        if not seen[v2]:
            cnt[v2] += x
            seen[v2] = True
            dq.append(v2)
print(*cnt[1:])