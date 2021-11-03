import sys
from collections import deque

_rl = sys.stdin.readline
_rl2 = lambda: [int(v) for v in _rl().split()]

M = int(_rl())
G = [[] for _ in range(10)]
for _ in range(M):
    u, v = _rl2()
    G[u].append(v)
    G[v].append(u)
P = _rl2()

init_p = 0
for n in P:
    init_p *= 10
    init_p += n
init_emp = 1
for n in sorted(P):
    if init_emp == n:
        init_emp += 1

seen = set()
seen.add(init_p)

q = deque()
q.append([init_p, init_emp, 0])
ans = -1
while len(q) > 0:
    p, emp, n = q.popleft()
    if p == 12345678:
        ans = n
        break
    plst = []
    while p > 0:
        d, m = divmod(p, 10)
        plst.append(m)
        p = d
    plst.reverse()
    for v2 in G[emp]:
        p2 = 0
        for _p in plst:
            p2 *= 10
            p2 += emp if _p == v2 else _p
        if p2 not in seen:
            seen.add(p2)
            q.append([p2, v2, n + 1])

print(ans)