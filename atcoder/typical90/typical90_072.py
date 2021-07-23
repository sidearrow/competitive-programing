split_int_input = lambda: [int(v) for v in input().split()]

H, W = split_int_input()
C = [[0 if v == "." else 1 for v in input()] for _ in range(H)]
# 0: 未探索平野
# 1: 山
# 2: 今回使用平野
# 3: 始点

d = [[0, 1], [1, 0], [0, -1], [-1, 0]]
ans = [-1]


def dfs(h, w, cnt):
    for _h, _w in d:
        _h += h
        _w += w
        if not (0 <= _h < H and 0 <= _w < W):
            continue
        if C[_h][_w] == 0:
            C[_h][_w] = 2
            dfs(_h, _w, cnt + 1)
            C[_h][_w] = 0
        if C[_h][_w] == 3 and cnt > 2:
            ans[0] = max(ans[0], cnt)


for h in range(H):
    for w in range(W):
        if C[h][w] != 1:
            C[h][w] = 3
            dfs(h, w, 1)
            C[h][w] = 0

print(ans[0])