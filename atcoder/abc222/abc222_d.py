import sys

readline = sys.stdin.readline
readline2 = lambda: [int(v) for v in readline().split()]

MOD = 998244353
N = int(readline())
A = readline2()
B = readline2()

MX = 3010
dp = [0] * MX

for i in range(A[0], B[0] + 1):
    dp[i] += 1
for i in range(MX - 1):
    dp[i + 1] += dp[i]
for i in range(1, N):
    a, b = A[i], B[i]
    for j in range(MX):
        if a <= j <= b:
            continue
        dp[j] = 0
    for j in range(MX - 1):
        dp[j + 1] += dp[j]
        dp[j + 1] %= MOD
print(dp[-1])
