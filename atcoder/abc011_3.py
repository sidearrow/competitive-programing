N = int(input())
NG = [int(input()) for _ in range(3)]

dp = [-1] * (N + 1)
dp[0] = 0
for i in range(1, N + 1):
    if i in NG:
        continue
    tmp = 200
    if i - 1 >= 0 and dp[i - 1] != -1 and dp[i - 1] < 100:
        tmp = min(tmp, dp[i - 1] + 1)
    if i - 2 >= 0 and dp[i - 2] != -1 and dp[i - 2] < 100:
        tmp = min(tmp, dp[i - 2] + 1)
    if i - 3 >= 0 and dp[i - 3] != -1 and dp[i - 3] < 100:
        tmp = min(tmp, dp[i - 3] + 1)
    if tmp <= 100:
        dp[i] = tmp

print("NO" if dp[N] == -1 else "YES")