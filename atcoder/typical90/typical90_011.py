import sys

readline = sys.stdin.readline
readline2 = lambda: [int(v) for v in readline().split()]

N = int(readline())
DCS = [readline2() for _ in range(N)]
DCS.sort(key=lambda v: v[0])

MAX_DAY = 5010

dp = [0] * (MAX_DAY + 1)
for d, c, s in DCS:
    for i in range(MAX_DAY, -1, -1):
        if c <= i <= d:
            dp[i] = max(dp[i], dp[i - c] + s)
print(max(dp))