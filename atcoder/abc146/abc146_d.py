from collections import deque

N = int(input())
G = [{} for _ in range(N + 1)]
AB = []
for _ in range(N - 1):
    a, b = [int(v) for v in input().split()]
    G[a][b] = -1
    G[b][a] = -1
    AB.append([a, b])

color_num = 0
for v in G:
    if len(v) > color_num:
        color_num = len(v)

dq = deque()
dq.append(1)
while len(dq) > 0:
    v1 = dq.pop()
    exist_colors = set()
    no_color_vs = deque()
    for v2, color in G[v1].items():
        if color == -1:
            dq.append(v2)
            no_color_vs.append(v2)
        else:
            exist_colors.add(color)
    j = 1
    while len(no_color_vs):
        if j not in exist_colors:
            v2 = no_color_vs.pop()
            G[v1][v2] = j
            G[v2][v1] = j
        j += 1

print(color_num)
for a, b in AB:
    print(G[a][b])
