MODINT = 10 ** 9 + 7
S = int(input())

dp = [0] * 2010
dp[3] = 1

for i in range(4, S + 1):
    tmp = 1
    for j in range(3, i - 2):
        tmp += dp[i - j]
    dp[i] = tmp % MODINT

print(dp[S])
