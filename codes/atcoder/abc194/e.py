import sys

input = sys.stdin.readline

N, M = [int(v) for v in input().split()]
A = [int(v) for v in input().split()]

res = None
for i in range(N - M + 1):
    tmp = A[i : i + M]
    _res = min(tmp) - 1
    if _res < 0:
        _res = max(A[0:M]) + 1
    if res is None:
        res = _res
    else:
        res = min(res, _res)

print(res)