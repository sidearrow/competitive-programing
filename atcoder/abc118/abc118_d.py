import sys

readline = sys.stdin.readline
readline2 = lambda: [int(v) for v in readline().split()]

N, M = readline2()
A = readline2()
A.sort()
B = [0, 2, 5, 5, 4, 5, 6, 3, 7, 6]

dp = [-1] * (N + 1)
dp[0] = 0
memo = [[0] * 10 for _ in range(N + 1)]
for i in range(1, N + 1):
    for a in A:
        b = B[a]
        if i - b >= 0 and dp[i - b] != -1 and dp[i - b] + 1 >= dp[i]:
            dp[i] = dp[i - b] + 1
            for j in range(10):
                tmp = memo[i - b][j]
                if j == a:
                    tmp += 1
                memo[i][j] = tmp

ans = []
for i in range(9, -1, -1):
    stri = str(i)
    for _ in range(memo[-1][i]):
        ans.append(stri)
print("".join(ans))