from collections import deque


split_int_input = lambda: [int(v) for v in input().split()]
INF = float("inf")


def get_dist_list():
    res = []
    for h in range(-2, 3):
        wrange = range(-1, 2) if h == -2 or h == 2 else range(-2, 3)
        for w in wrange:
            if not (h == 0 and w == 0):
                res.append([h, w])
    return res


H, W = split_int_input()
S = [input() for _ in range(H)]

dist_list = get_dist_list()
G = [{} for _ in range(H * W)]
for h in range(H):
    for w in range(W):
        a_idx = h * W + w
        for _h, _w in dist_list:
            h2 = h + _h
            w2 = w + _w
            if not (0 <= h2 < H and 0 <= w2 < W):
                continue
            b_idx = h2 * W + w2
            if b_idx not in G[a_idx]:
                G[a_idx][b_idx] = 1
            if a_idx not in G[b_idx]:
                G[b_idx][a_idx] = 1
        for _h, _w in [[1, 0], [0, 1], [-1, 0], [0, -1]]:
            h2 = h + _h
            w2 = w + _w
            if not (0 <= h2 < H and 0 <= w2 < W):
                continue
            if S[h2][w2] == ".":
                b_idx = h2 * W + w2
                G[a_idx][b_idx] = 0

dq = deque([0])
dist = [INF] * (H * W)
dist[0] = 0
while len(dq) > 0:
    v = dq.popleft()
    for v2, c in G[v].items():
        d = dist[v] + c
        if d < dist[v2]:
            dist[v2] = d
            if c == 0:
                dq.appendleft(v2)
            else:
                dq.append(v2)

print(dist[-1])