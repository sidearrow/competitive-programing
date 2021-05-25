from collections import deque

split_int_input = lambda: [int(v) for v in input().split()]

N = int(input())
G = [[] for _ in range(N + 1)]
for _ in range(N - 1):
    u, v, w = split_int_input()
    G[u].append([v, w])
    G[v].append([u, w])

ans = [-1] * (N + 1)
dq = deque([1])
ans[1] = 0
while len(dq) > 0:
    v = dq.popleft()
    c = ans[v]
    for v2, w2 in G[v]:
        if ans[v2] == -1:
            dq.append(v2)
            ans[v2] = (w2 & 1) ^ c

print(*ans[1:], sep="\n")