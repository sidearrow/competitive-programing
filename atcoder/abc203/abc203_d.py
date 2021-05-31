import sys
from typing import List

readline = sys.stdin.readline
split_int_readline = lambda: [int(v) for v in readline().split()]


def twod_prefix_sum(a: List[List[int]]):
    for i in range(len(a)):
        for j in range(len(a[i])):
            tmp = a[i][j]
            if i - 1 >= 0:
                tmp += a[i - 1][j]
            if j - 1 >= 0:
                tmp += a[i][j - 1]
            if i - 1 >= 0 and j - 1 >= 0:
                tmp -= a[i - 1][j - 1]
            a[i][j] = tmp
    return a


def twod_prefix_sum_get_range(a: List[List[int]], r1: int, c1: int, r2: int, c2: int):
    res = a[r2][c2]
    if r1 - 1 >= 0 and c1 - 1 >= 0:
        res += a[r1 - 1][c1 - 1]
    if r1 - 1 >= 0:
        res -= a[r1 - 1][c2]
    if c1 - 1 >= 0:
        res -= a[r2][c1 - 1]
    return res


N, K = split_int_readline()
A = [split_int_readline() for _ in range(N)]

l = -1
r = 10 ** 9
k = K ** 2 // 2
while r - l > 1:
    mid = (l + r) // 2
    a = [[int(A[i][j] > mid) for j in range(N)] for i in range(N)]
    a = twod_prefix_sum(a)
    valid = False
    for i in range(N - K + 1):
        for j in range(N - K + 1):
            res = twod_prefix_sum_get_range(a, i, j, i + K - 1, j + K - 1)
            if res <= k:
                valid = True
    if valid:
        r = mid
    else:
        l = mid

print(r)