split_int_input = lambda: [int(v) for v in input().split()]

N = int(input())
A = [split_int_input() for _ in range(N)]

memo = [[0] * N for _ in range(N)]
for i in range(N):
    for j in range(N):
        memo[i][j] = (
            abs(A[j][0] - A[i][0]) + abs(A[j][1] - A[i][1]) + max(0, A[j][2] - A[i][2])
        )


INF = float("inf")
dp = [[INF] * N for _ in range(2 ** N)]
dp[1][0] = 0
for bit in range(2 ** N):
    for i in range(N):
        if bit >> i & 1:
            for j in range(N):
                if bit >> j & 1:
                    continue
                next_bit = bit | (1 << j)
                dp[next_bit][j] = min(dp[next_bit][j], dp[bit][i] + memo[i][j])
ans = INF
for i, v in enumerate(dp[-1]):
    ans = min(ans, v + memo[i][0])
print(ans)