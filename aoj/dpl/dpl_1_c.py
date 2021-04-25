split_int_input = lambda: [int(v) for v in input().split()]

N, W = split_int_input()
A = [split_int_input() for _ in range(N)]

dp = [0] * (W + 1)
for i in range(1, W + 1):
    for v, w in A:
        if i - w >= 0:
            dp[i] = max(dp[i], dp[i - 1], dp[i - w] + v)
        else:
            dp[i] = max(dp[i], dp[i - 1])

print(dp[-1])
