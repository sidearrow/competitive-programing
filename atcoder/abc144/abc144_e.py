import sys

_rl = sys.stdin.readline
_rl2 = lambda: [int(v) for v in _rl().split()]

N, K = _rl2()
A = _rl2()
F = _rl2()

A.sort()
F.sort(reverse=True)


def check(x):
    k = K
    for i in range(N):
        if A[i] * F[i] > x:
            k -= A[i] - x // F[i]
            if k < 0:
                return False
    return True


l = -1
r = A[-1] * F[0]

while r - l > 1:
    m = (r + l) // 2
    if check(m):
        r = m
    else:
        l = m
print(r)