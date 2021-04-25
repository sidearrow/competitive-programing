split_int_input = lambda: [int(v) for v in input().split()]

N, W = split_int_input()
A = [split_int_input() for _ in range(N)]

V_SUM = sum([v for v, _ in A])
dp = [W + 1] * (V_SUM + 1)
dp[0] = 0
for v, w in A:
    for i in range(V_SUM, v - 1, -1):
        dp[i] = min(dp[i], dp[i - v] + w)

ans = 0
for v, w in enumerate(dp):
    if w != W + 1:
        ans = v

print(ans)