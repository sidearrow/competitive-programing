"""
https://onlinejudge.u-aizu.ac.jp/problems/GRL_1_C
https://onlinejudge.u-aizu.ac.jp/status/users/sidearrow/submissions/1/GRL_1_C/judge/5705533/Python3
"""

INF = float("inf")

# 入力、初期化
V, E = map(int, input().split())
dp = [[INF] * V for _ in range(V)]
for _ in range(E):
    s, t, d = map(int, input().split())
    dp[s][t] = d
for v in range(V):
    dp[v][v] = 0

# DP 遷移
for k in range(V):
    for i in range(V):
        for j in range(V):
            dp[i][j] = min(dp[i][j], dp[i][k] + dp[k][j])

# 負閉路の有無をチェック
for v in range(V):
    if dp[v][v] < 0:
        print("NEGATIVE CYCLE")
        exit()

# 出力
for a in dp:
    print(*["INF" if b == INF else b for b in a])