import sys

readline = sys.stdin.readline
split_int_readline = lambda: [int(v) for v in readline().split()]

N, K = split_int_readline()
H = split_int_readline()
INF = float("inf")

dp = [INF] * N
dp[0] = 0
for i in range(N - 1):
    for j in range(1, K + 1):
        j += i
        if j < N:
            dp[j] = min(dp[j], dp[i] + abs(H[i] - H[j]))

print(dp[-1])