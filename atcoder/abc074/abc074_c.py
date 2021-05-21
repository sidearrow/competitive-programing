split_int_input = lambda: [int(v) for v in input().split()]

A, B, C, D, E, F = split_int_input()
A *= 100
B *= 100
E /= 100
dp = [[-1, -1, -1] for _ in range(F + 1)]
dp[0] = [0, 0, 0]
for i in range(1, F + 1):
    for x in [A, B]:
        if i - x < 0 or dp[i - x][0] == -1:
            continue
        a, b, c = dp[i - x]
        a += x
        dp[i] = [a, b, c]
    for x in [C, D]:
        if i - x < 0 or dp[i - x][0] <= 0:
            continue
        a, b, c = dp[i - x]
        b += x
        c = b / a
        if c <= E:
            dp[i] = [a, b, c]

dp = sorted(dp, key=lambda v: v[2])
a, b, _ = dp[-1]
print(a + b, b)