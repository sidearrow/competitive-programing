from bisect import bisect_left

input_split_int = lambda: [int(v) for v in input().split()]

N, M = input_split_int()
G = [[] for _ in range(N)]
for _ in range(M):
    a, b = input_split_int()
    G[a - 1].append(b - 1)
    G[b - 1].append(a - 1)

for i in range(N):
    G[i] = sorted(G[i])

ans = 0
for i in range(N):
    if bisect_left(G[i], i) == 1:
        ans += 1

print(ans)