split_int_input = lambda: [int(v) for v in input().split()]


def warshall_floyd(n, dist):
    for k in range(n):
        for i in range(n):
            for j in range(n):
                dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])


def exist_negative_cycle(n, dist):
    for i in range(n):
        if dist[i][i] < 0:
            return True
    return False


INF = float("INF")
V, E = split_int_input()
dist = [[INF] * V for _ in range(V)]
for _ in range(E):
    s, t, d = split_int_input()
    dist[s][t] = d
for i in range(V):
    dist[i][i] = 0

warshall_floyd(V, dist)

if exist_negative_cycle(V, dist):
    print("NEGATIVE CYCLE")
else:
    for r in dist:
        print(*["INF" if v == INF else v for v in r])