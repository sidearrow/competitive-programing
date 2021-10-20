import sys

_rl = sys.stdin.readline
_rl2 = lambda: [int(v) for v in _rl().split()]

N = int(_rl())
A = _rl2()

memo = [0] * (N + 1)
for i in range(N):
    if i % 2:
        memo[i] = memo[i - 1] - A[i]
    else:
        memo[i] = memo[i - 1] + A[i]

memo2 = {}
for v in memo:
    if v not in memo2:
        memo2[v] = 0
    memo2[v] += 1

ans = 0
for v in memo2.values():
    ans += v * (v - 1) // 2

print(ans)
