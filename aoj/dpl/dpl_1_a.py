split_int_input = lambda: [int(v) for v in input().split()]

N, M = split_int_input()
C = split_int_input()

dp = [50010] * (N + 1)
dp[0] = 0

for i in range(1, N + 1):
    for c in C:
        if i - c >= 0:
            dp[i] = min(dp[i], dp[i - c] + 1)

print(dp[-1])