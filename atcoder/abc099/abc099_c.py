N = int(input())

a = [1]
tmp = 6
while tmp <= N:
    a.append(tmp)
    tmp *= 6
tmp = 9
while tmp <= N:
    a.append(tmp)
    tmp *= 9

dp = [10 ** 5 + 10] * (N + 1)
dp[0] = 0
for i in range(N + 1):
    for v in a:
        if i - v >= 0:
            dp[i] = min(dp[i], dp[i - v] + 1)

print(dp[-1])
