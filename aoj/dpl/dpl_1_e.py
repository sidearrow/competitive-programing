S1 = input()
S2 = input()
LS1 = len(S1)
LS2 = len(S2)

dp = [[10 ** 5] * (LS1 + 1) for _ in range(LS2 + 1)]
dp[0][0] = 0
for i in range(LS2 + 1):
    for j in range(LS1 + 1):
        if i > 0 and j > 0:
            if S2[i - 1] == S1[j - 1]:
                dp[i][j] = min(dp[i][j], dp[i - 1][j - 1])
            else:
                dp[i][j] = min(dp[i][j], dp[i - 1][j - 1] + 1)
        if j > 0:
            dp[i][j] = min(dp[i][j], dp[i][j - 1] + 1)
        if i > 0:
            dp[i][j] = min(dp[i][j], dp[i - 1][j] + 1)

print(dp[-1][-1])