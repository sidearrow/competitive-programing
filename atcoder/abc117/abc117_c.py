import sys

readline = sys.stdin.readline
readline2 = lambda: [int(v) for v in readline().split()]

N, M = readline2()
X = readline2()
X.sort()

dx = sorted([X[i + 1] - X[i] for i in range(M - 1)], reverse=True)
ans = sum(dx[N - 1 :])
print(ans)
