import sys
from collections import Counter


def ncr(n, r):
    res = 1
    for i in range(n, n - r, -1):
        res *= i
    for i in range(1, r + 1):
        res //= i
    return res


_rl = sys.stdin.readline
_rl2 = lambda: [int(v) for v in _rl().split()]

N, A, B = _rl2()
V = _rl2()
V.sort()
V.reverse()

avg = sum(V[:A]) / A
print(avg)

cntrv = Counter(V)
mx = max(cntrv.keys())
mn = V[A - 1]
mn_num = cntrv[mn]

if mn != max(cntrv.keys()):
    cnt = 0
    for v, n in cntrv.items():
        if v > mn:
            cnt += n
    r = A - cnt
    ans = ncr(mn_num, r)
    print(ans)
    exit()

l = min(A, mn_num)
r = min(B, mn_num)
ans = 0
for r in range(l, r + 1):
    ans += ncr(mn_num, r)
print(ans)
