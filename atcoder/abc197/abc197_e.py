import sys

_rl = sys.stdin.readline
_rl2 = lambda: [int(v) for v in _rl().split()]

N = int(_rl())
XC = [_rl2() for _ in range(N)]
XC.sort(key=lambda v: v[0])

A = [[] for _ in range(N + 1)]
for x, c in XC:
    A[c].append(x)
A[0].append(0)

memo = [[0, 0] for _ in range(N + 1)]
l1, r1 = 0, 0
for i in range(1, N + 1):
    if len(A[i]) == 0:
        memo[i][0] = memo[i - 1][0]
        memo[i][1] = memo[i - 1][1]
        continue
    l2, r2 = A[i][0], A[i][-1]
    ll = memo[i - 1][0] + abs(l1 - r2) + (r2 - l2)
    rl = memo[i - 1][1] + abs(r1 - r2) + (r2 - l2)
    lr = memo[i - 1][0] + abs(l1 - l2) + (r2 - l2)
    rr = memo[i - 1][1] + abs(r1 - l2) + (r2 - l2)
    memo[i][0] = min(ll, rl)
    memo[i][1] = min(lr, rr)
    l1, r1 = l2, r2
ans = min(memo[-1][0] + abs(l1), memo[-1][1] + abs(r1))
print(ans)