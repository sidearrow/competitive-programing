import sys
from collections import deque

_rl = sys.stdin.readline
_rl2 = lambda: [int(v) for v in _rl().split()]

N, Q = _rl2()

a = [[-1, -1] for _ in range(N + 1)]
for _ in range(Q):
    q = _rl2()
    if q[0] == 1:
        x, y = q[1:]
        a[x][1] = y
        a[y][0] = x
    elif q[0] == 2:
        x, y = q[1:]
        a[x][1] = -1
        a[y][0] = -1
    else:
        x = q[1]
        ans = deque([x])
        l = a[x][0]
        while l != -1:
            ans.appendleft(l)
            l = a[l][0]
        r = a[x][1]
        while r != -1:
            ans.append(r)
            r = a[r][1]
        print(len(ans), *ans)
