import collections

split_int_input = lambda: [int(v) for v in input().split()]

N = int(input())
G = [[] for _ in range(N)]
for _ in range(N - 1):
    a, b = split_int_input()
    a, b = a - 1, b - 1
    G[a].append(b)
    G[b].append(a)

v_status = [-1] * N
dq = collections.deque()
dq.append(0)
v_status[0] = 0
is_bipartite = True
while len(dq) > 0:
    v = dq.popleft()
    for v2 in G[v]:
        if v_status[v2] == -1:
            v_status[v2] = v_status[v] ^ 1
            dq.append(v2)
        else:
            if v_status[v] == v_status[v2]:
                is_bipartite = False
                break

ans = [[], []]
cnt = 0
for i, v in enumerate(v_status, 1):
    if v == 0 or v == 1:
        ans[v].append(i)

ansidx = 0
if len(ans[0]) < len(ans[1]):
    ansidx = 1

print(*ans[ansidx][: N // 2])
