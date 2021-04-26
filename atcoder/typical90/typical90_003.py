import collections

split_int_input = lambda: [int(v) for v in input().split()]

N = int(input())
G = [[] for _ in range(N)]
for _ in range(N - 1):
    a, b = split_int_input()
    G[a - 1].append(b - 1)
    G[b - 1].append(a - 1)


def bfs(start):
    res = [-1] * N
    seen = [False] * N
    dq = collections.deque()
    dq.append([start, 0])
    seen[start] = True
    while len(dq) > 0:
        v, l = dq.popleft()
        res[v] = l
        for v2 in G[v]:
            if not seen[v2]:
                dq.append([v2, l + 1])
                seen[v2] = True
    return res


res = bfs(0)
idx = res.index(max(res))
res = bfs(idx)
ans = max(res) + 1

print(ans)