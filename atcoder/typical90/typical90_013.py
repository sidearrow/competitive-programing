import heapq

split_int_input = lambda: [int(v) for v in input().split()]

N, M = split_int_input()
G = [[] for _ in range(N)]
for _ in range(M):
    a, b, c = split_int_input()
    a, b = a - 1, b - 1
    G[a].append([b, c])
    G[b].append([a, c])


def dijkstra(start_v):
    dist = [10 ** 10] * N
    dist[start_v] = 0
    hq = [[0, start_v]]
    while len(hq) > 0:
        d, v = heapq.heappop(hq)
        if d > dist[v]:
            continue
        for v2, d2 in G[v]:
            d2 += d
            if d2 < dist[v2]:
                heapq.heappush(hq, [d2, v2])
                dist[v2] = d2
    return dist


dist1 = dijkstra(0)
dist2 = dijkstra(N - 1)

for i in range(N):
    print(dist1[i] + dist2[i])