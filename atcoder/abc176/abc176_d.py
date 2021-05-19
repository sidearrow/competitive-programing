from collections import deque

split_int_input = lambda: [int(v) for v in input().split()]

H, W = split_int_input()
C = split_int_input()
D = split_int_input()
S = [[s for s in input()] for _ in range(H)]

dq = deque([(C[0] - 1, C[1] - 1, 0)])
seen = [[False] * W for _ in range(H)]
while len(dq) > 0:
    h, w, d = dq.popleft()
    if S[h][w] != "." and S[h][w] <= d:
        continue
    S[h][w] = d
    for _h in range(max(0, h - 2), min(H, h + 3)):
        for _w in range(max(0, w - 2), min(W, w + 3)):
            if S[_h][_w] != ".":
                continue
            if abs(h - _h) + abs(w - _w) <= 1:
                dq.appendleft((_h, _w, d))
            else:
                dq.append((_h, _w, d + 1))

ans = S[D[0] - 1][D[1] - 1]
print(-1 if ans == "." else ans)
