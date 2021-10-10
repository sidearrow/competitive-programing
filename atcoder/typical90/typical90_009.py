import sys
import math
from bisect import bisect_left

readline = sys.stdin.readline
readline2 = lambda: [int(v) for v in readline().split()]

N = int(readline())
XY = [readline2() for _ in range(N)]


def conv(d):
    return d if d <= 180 else 360 - d


ans = 0
for i in range(N):
    x, y = XY[i]
    degs = []
    for j in range(N):
        if i != j:
            _x, _y = XY[j]
            deg = math.degrees(math.atan2(_y - y, _x - x)) % 360
            degs.append(deg)
    degs.sort()
    for j in range(N - 1):
        d1 = degs[j]
        idx = bisect_left(degs, (d1 + 180) % 360)
        d2 = 0
        if idx - 1 >= 0:
            d2 = max(d2, conv(abs(degs[idx - 1] - d1)))
        if idx < N - 1:
            d2 = max(d2, conv(abs(degs[idx] - d1)))
        if d2 > ans:
            ans = d2

print(ans)
