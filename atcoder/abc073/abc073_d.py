import sys
from itertools import permutations

readline = sys.stdin.readline
readline2 = lambda: [int(v) for v in readline().split()]

INF = float("inf")
N, M, R = readline2()
R2 = readline2()
E = [readline2() for _ in range(M)]


def main():
    memo = [[INF] * N for _ in range(N)]
    for a, b, c in E:
        memo[a - 1][b - 1] = c
        memo[b - 1][a - 1] = c
    for i in range(N):
        memo[i][i] = 0
    for a in range(N):
        for b in range(N):
            for c in range(N):
                tmp = memo[b][a] + memo[a][c]
                if memo[b][c] > tmp:
                    memo[b][c] = tmp
    ans = float("inf")
    for v in permutations(range(R)):
        tmp = 0
        for i in range(R - 1):
            l, r = R2[v[i]] - 1, R2[v[i + 1]] - 1
            tmp += memo[l][r]
        if tmp < ans:
            ans = tmp
    print(ans)


main()