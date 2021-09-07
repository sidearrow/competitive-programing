from bisect import bisect_left
from collections import defaultdict

MOD = 10 ** 9 + 7
N = int(input())
C = [int(input()) for _ in range(N)]

c_idx = defaultdict(list)
for i, c in enumerate(C):
    c_idx[c].append(i)

dp = [0] * N
dp[0] = 1
for i in range(1, N):
    c = C[i]
    dp[i] = dp[i - 1]
    idx2 = bisect_left(c_idx[c], i)
    if idx2 > 0 and i - c_idx[c][idx2 - 1] > 1:
        dp[i] = (dp[i] + dp[c_idx[c][idx2 - 1]]) % MOD

print(dp[-1])
