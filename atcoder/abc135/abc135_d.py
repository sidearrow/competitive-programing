S = list(reversed([c for c in input()]))
MOD = 10 ** 9 + 7

dp = [0] * 13
if S[0] == "?":
    for i in range(10):
        dp[i] = 1
else:
    dp[int(S[0])] = 1


tmp = 10
for i in range(1, len(S)):
    new_dp = [0] * 13
    s = S[i]
    if s == "?":
        for j in range(10):
            b = tmp * j % 13
            for k, v in enumerate(dp):
                new_dp[(b + k) % 13] += v
    else:
        b = tmp * int(s) % 13
        for j, v in enumerate(dp):
            new_dp[(b + j) % 13] += v
    tmp = tmp * 10 % 13
    dp = [v % MOD for v in new_dp]

print(dp[5])