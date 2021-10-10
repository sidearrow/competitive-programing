import sys

sys.setrecursionlimit(10 ** 7)
readline = sys.stdin.readline
readline2 = lambda: [int(v) for v in readline().split()]

MOD = 998244353
N, M, K = readline2()
A = readline2()
G = [[] for _ in range(N + 1)]
for i in range(N - 1):
    u, v = readline2()
    G[u].append([v, i])
    G[v].append([u, i])

memo = [0] * (N - 1)
seen = [False] * (N + 1)
edge = [False] * (N - 1)


def dfs(v, goal):
    if v == goal:
        return True
    for v2, e in G[v]:
        if not seen[v2]:
            seen[v2] = True
            res = dfs(v2, goal)
            if res:
                memo[e] += 1
                return True
    return False


for i in range(M - 1):
    a, b = A[i], A[i + 1]
    seen[a] = True
    dfs(a, b)
    for i in range(N + 1):
        seen[i] = False
    for i in range(N - 1):
        edge[i] = False

memosum = sum(memo)
if (memosum + K) % 2 == 1:
    print(0)
    exit()
a = (memosum + K) // 2
b = memosum - a
if a < 0 or b < 0:
    print(0)
    exit()
a = min(a, b)

dp = [0] * (a + 1)
dp[0] = 1
for i in range(N - 1):
    m = memo[i]
    for j in range(a, m - 1, -1):
        dp[j] += dp[j - m]
        dp[j] %= MOD

print(dp[-1])