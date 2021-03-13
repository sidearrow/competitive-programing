import sys

input = sys.stdin.readline

N, K = [int(v) for v in input().split()]


def solve(n: int):
    n = str(n)
    tmp = [0] * 10
    for a in n:
        tmp[int(a)] += 1
    mn = ""
    for i, v in enumerate(tmp):
        mn += str(i) * v
    mx = "".join(list(reversed(mn)))
    res = int(mx) - int(mn)
    return res


res = N
for _ in range(K):
    res = solve(res)

print(res)