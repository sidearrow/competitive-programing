import sys

sys.setrecursionlimit(10 ** 7)
split_int_input = lambda: [int(v) for v in input().split()]

N = int(input())
G = [[] for _ in range(N + 1)]
for _ in range(N - 1):
    a, b = split_int_input()
    G[a].append(b)
    G[b].append(a)

for i in range(N + 1):
    G[i] = sorted(G[i])

seen = [False] * (N + 1)
ans = []


def dfs(a):
    ans.append(a)
    seen[a] = True
    for a1 in G[a]:
        if seen[a1] is False:
            dfs(a1)
            ans.append(a)


dfs(1)
print(*ans)