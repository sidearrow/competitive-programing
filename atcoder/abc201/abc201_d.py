split_int_input = lambda: [int(v) for v in input().split()]
INF = float("inf")

H, W = split_int_input()
A = []
for _ in range(H):
    A.append([1 if s == "+" else -1 for s in input()])

dp = [[None] * W for _ in range(H)]
for h in range(H - 1, -1, -1):
    for w in range(W - 1, -1, -1):
        if h == H - 1 and w == W - 1:
            dp[h][w] = 0
            continue
        if (h + w) % 2:
            dp[h][w] = INF
            if h < H - 1:
                dp[h][w] = min(dp[h][w], dp[h + 1][w] - A[h + 1][w])
            if w < W - 1:
                dp[h][w] = min(dp[h][w], dp[h][w + 1] - A[h][w + 1])
        else:
            dp[h][w] = -INF
            if h < H - 1:
                dp[h][w] = max(dp[h][w], dp[h + 1][w] + A[h + 1][w])
            if w < W - 1:
                dp[h][w] = max(dp[h][w], dp[h][w + 1] + A[h][w + 1])

if dp[0][0] > 0:
    print("Takahashi")
elif dp[0][0] < 0:
    print("Aoki")
else:
    print("Draw")