split_int_input = lambda: [int(v) for v in input().split()]


def bellman_ford(graph, v_num, start_v):
    INF = float("INF")
    dist = [INF] * v_num
    dist[start_v] = 0
    exist_negative_cycle = False
    for i in range(v_num):
        update = False
        for v in range(v_num):
            if dist[v] == INF:
                continue
            for v2, v2d in graph[v]:
                v2d += dist[v]
                if dist[v2] > v2d:
                    dist[v2] = v2d
                    update = True
        if not update:
            break
        if update and i == v_num - 1:
            exist_negative_cycle = True
    return exist_negative_cycle, dist


V, E, R = split_int_input()
G = [[] for _ in range(V)]
for _ in range(E):
    s, t, d = split_int_input()
    G[s].append([t, d])

ng, dist = bellman_ford(G, V, R)

if ng:
    print("NEGATIVE CYCLE")
else:
    for v in dist:
        print("INF" if v == float("INF") else v)
