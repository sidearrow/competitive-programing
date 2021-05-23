from collections import deque

split_int_input = lambda: [int(v) for v in input().split()]

N = int(input())
G = [[] for _ in range(N + 1)]
for _ in range(N - 1):
    a, b = split_int_input()
    G[a].append(b)
    G[b].append(a)
C = sorted(split_int_input(), reverse=True)

dq = deque()
seen = [False] * (N + 1)
ans = [0] * (N + 1)
dq.append(1)
seen[1] = True
cidx = 0
while len(dq) > 0:
    v = dq.popleft()
    ans[v] = C[cidx]
    cidx += 1
    for v2 in G[v]:
        if not seen[v2]:
            dq.append(v2)
            seen[v2] = True

print(sum(ans[2:]))
print(*ans[1:])