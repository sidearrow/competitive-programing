import sys
import math

_rl = sys.stdin.readline
_rl2 = lambda: [int(v) for v in _rl().split()]

N = int(_rl())
XY = [_rl2() for _ in range(N)]

ans = set()
for i in range(N):
    for j in range(N):
        if i == j:
            continue
        x1, y1 = XY[i]
        x2, y2 = XY[j]
        x = x2 - x1
        y = y2 - y1
        _gcd = math.gcd(x, y)
        ans.add((x // _gcd, y // _gcd))

print(len(ans))