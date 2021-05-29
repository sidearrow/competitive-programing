split_int_input = lambda: [int(v) for v in input().split()]

H, W = split_int_input()
S = [input() for _ in range(H)]

ans = [[1] * W for _ in range(H)]
memo = [[[1] * W for _ in range(H)] for _ in range(3)]
dir = [[-1, 0], [0, -1], [-1, -1]]
mod = 10 ** 9 + 7
for h in range(H):
    for w in range(W):
        if h == 0 and w == 0:
            continue
        tmp = 0
        for i, (_h, _w) in enumerate(dir):
            _h += h
            _w += w
            if _h >= 0 and _w >= 0 and S[_h][_w] == ".":
                tmp += memo[i][_h][_w]
        ans[h][w] = tmp % mod
        for i, (_h, _w) in enumerate(dir):
            _h += h
            _w += w
            if _h >= 0 and _w >= 0 and S[_h][_w] == ".":
                memo[i][h][w] = (memo[i][_h][_w] + tmp) % mod
            else:
                memo[i][h][w] = tmp

print(ans[-1][-1])