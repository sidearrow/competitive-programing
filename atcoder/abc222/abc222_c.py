import sys

readline = sys.stdin.readline
readline2 = lambda: [int(v) for v in readline().split()]


def jnk(a, b):
    if a == b:
        return 0
    if a == "G":
        if b == "C":
            return 1
        else:
            return -1
    if a == "C":
        if b == "P":
            return 1
        else:
            return -1
    if a == "P":
        if b == "G":
            return 1
        else:
            return -1


N, M = readline2()
A = [readline().rstrip() for _ in range(2 * N)]


memo = [0] * (2 * N)
memo2 = list(range(2 * N))
for i in range(M):
    for j in range(N):
        a, b = memo2[j * 2], memo2[j * 2 + 1]
        res = jnk(A[a][i], A[b][i])
        if res == 1:
            memo[a] += 1
        elif res == -1:
            memo[b] += 1
    memo3 = [[v, -i] for i, v in enumerate(memo)]
    memo3.sort(key=lambda v: (v[0], v[1]), reverse=True)
    memo2 = [-i for _, i in memo3]

for v in memo2:
    print(v + 1)
