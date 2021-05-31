import sys

readline = sys.stdin.readline

N = int(readline())
H = [int(v) for v in readline().split()]
INF = float("inf")

dp = [INF] * N
dp[0] = 0

for i, h in enumerate(H[1:], 1):
    dp[i] = min(dp[i], dp[i - 1] + abs(H[i] - H[i - 1]))
    if i - 2 >= 0:
        dp[i] = min(dp[i], dp[i - 2] + abs(H[i] - H[i - 2]))

print(dp[-1])
