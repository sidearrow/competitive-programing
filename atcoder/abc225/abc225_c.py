import sys

_rl = sys.stdin.readline
_rl2 = lambda: [int(v) for v in _rl().split()]


N, M = _rl2()


def check(b):
    for i in range(1, M):
        if b[i - 1] + 1 != b[i]:
            return False
        if b[i] % 7 == 1:
            return False
    return True


res = True
prevtop = -1
for i in range(N):
    b = _rl2()
    if i > 0:
        if b[0] != prevtop + 7:
            res = False
    if not check(b):
        res = False
    prevtop = b[0]


print("Yes" if res else "No")