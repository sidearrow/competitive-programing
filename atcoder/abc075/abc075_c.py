from collections import deque

split_int_input = lambda: [int(v) for v in input().split()]
N, M = split_int_input()
EDGES = []
for _ in range(M):
    a, b = split_int_input()
    EDGES.append((a - 1, b - 1))

ans = 0
for i in range(M):
    g = [[] for _ in range(N)]
    for j, (a, b) in enumerate(EDGES):
        if i != j:
            g[a].append(b)
            g[b].append(a)
    seen = [False] * (N)
    seen[0] = True
    q = deque([0])
    cnt = 0
    while len(q) > 0:
        cnt += 1
        p = q.popleft()
        for nextp in g[p]:
            if seen[nextp]:
                continue
            seen[nextp] = True
            q.append(nextp)
    if cnt != N:
        ans += 1

print(ans)
