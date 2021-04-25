split_int_input = lambda: [int(v) for v in input().split()]

N, W = split_int_input()
A = [split_int_input() for _ in range(N)]

dp = [[0] * (W + 1) for _ in range(N + 1)]
for i, (v, w) in enumerate(A, 1):
    for j in range(1, W + 1):
        if j - w >= 0:
            dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - w] + v)
        else:
            dp[i][j] = dp[i - 1][j]

print(dp[-1][-1])