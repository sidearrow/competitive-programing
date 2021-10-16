import sys

readline = sys.stdin.readline
readline2 = lambda: [int(v) for v in readline().split()]

MOD = 998244353
N, K = readline2()
memo = [0] * (N + 1)
memo2 = [0] * N
for _ in range(K):
    c, k = readline().split()
    k = int(k)
    if c == "L":
        memo2[k - 1] = 1
        memo[k - 1] += 1
        memo[-1] -= 1
    else:
        memo2[k - 1] = 1
        memo[0] += 1
        memo[k] -= 1
for i in range(N):
    memo[i + 1] += memo[i]

ans = 1
for i in range(N):
    if memo2[i] == 1:
        ans *= 1
    else:
        ans *= memo[i]
        ans %= MOD
print(ans)