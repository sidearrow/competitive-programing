split_int_input = lambda: [int(v) for v in input().split()]
INF = float("inf")

N, P, K = split_int_input()
A = [split_int_input() for _ in range(N)]
MAX_X = 10 ** 15


def calc_cnt(x):
    dp = [[INF] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            dp[i][j] = x if A[i][j] == -1 else A[i][j]
    for a in range(N):
        for i in range(N):
            for j in range(N):
                dp[i][j] = min(dp[i][j], dp[i][a] + dp[a][j])
    cnt = 0
    for i in range(N):
        for j in range(i + 1, N):
            if dp[i][j] <= P:
                cnt += 1
    return cnt


def calc_x(k):
    l = 0
    r = MAX_X
    while r - l > 1:
        m = (r + l) // 2
        cnt = calc_cnt(m)
        if cnt <= k:
            r = m
        else:
            l = m
    return r


l = calc_x(K)
r = calc_x(K - 1)
if l == MAX_X and r == MAX_X:
    print(0)
elif r == MAX_X:
    print("Infinity")
else:
    print(r - l)
