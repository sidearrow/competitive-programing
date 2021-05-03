import sys

sys.setrecursionlimit(10 ** 7)

split_int_input = lambda: [int(v) for v in input().split()]
N = int(input())
C = split_int_input()
T = [[] for _ in range(N)]
for _ in range(N - 1):
    a, b = split_int_input()
    a -= 1
    b -= 1
    T[a].append(b)
    T[b].append(a)

colors = [0] * (10 ** 5 + 10)
seen = [False] * (10 ** 5 + 10)
ans = []


def dfs(to):
    seen[to] = True
    c = C[to]
    if colors[c] == 0:
        ans.append(to)
    colors[c] += 1
    for v in T[to]:
        if not seen[v]:
            dfs(v)
    colors[c] -= 1


dfs(0)


for v in sorted(ans):
    print(v + 1)