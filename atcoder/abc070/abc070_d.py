import sys
from collections import deque

input = sys.stdin.readline
split_int_input = lambda: [int(v) for v in input().split()]

N = int(input())
G = [[] for _ in range(N + 1)]
for _ in range(N - 1):
    a, b, c = split_int_input()
    G[a].append([b, c])
    G[b].append([a, c])
Q, K = split_int_input()


dq = deque()
dq.append([K, 0])
dist = [-1] * (N + 1)
while len(dq) > 0:
    v, d = dq.popleft()
    dist[v] = d
    for v2, d2 in G[v]:
        d2 += d
        if dist[v2] == -1:
            dq.append([v2, d2])

for _ in range(Q):
    x, y = split_int_input()
    print(dist[x] + dist[y])