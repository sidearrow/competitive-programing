import sys

_rl = sys.stdin.readline

N, S = _rl().split()
N = int(N)
S.rsplit()

a = {"A": 0, "C": 1, "G": 2, "T": 3}

memo = [[0] * 4 for _ in range(N + 1)]
for i, s in enumerate(S, 1):
    for j in range(4):
        memo[i][j] = memo[i - 1][j]
        if j == a[s]:
            memo[i][j] += 1

ans = 0
for i in range(N):
    for j in range(i + 1, N + 1):
        tmp = [0] * 4
        for k in range(4):
            tmp[k] = memo[j][k] - memo[i][k]
        if tmp[0] == tmp[3] and tmp[1] == tmp[2]:
            ans += 1

print(ans)