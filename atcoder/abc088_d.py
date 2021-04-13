from collections import deque

split_int_input = lambda: [int(v) for v in input().split()]
H, W = split_int_input()
s = [input() for _ in range(H)]

seen = [[False] * W for _ in range(H)]
dq = deque()
dq.append([0, 0, 1])
seen[0][0] = True
hw_len = -1
while 1:
    h, w, l = dq.popleft()
    if h == H - 1 and w == W - 1:
        hw_len = l
        break
    if h + 1 < H and s[h + 1][w] == "." and not seen[h + 1][w]:
        seen[h + 1][w] = True
        dq.append([h + 1, w, l + 1])
    if w + 1 < W and s[h][w + 1] == "." and not seen[h][w + 1]:
        seen[h][w + 1] = True
        dq.append([h, w + 1, l + 1])
    if h - 1 >= 0 and s[h - 1][w] == "." and not seen[h - 1][w]:
        seen[h - 1][w] = True
        dq.append([h - 1, w, l + 1])
    if w - 1 >= 0 and s[h][w - 1] == "." and not seen[h][w - 1]:
        seen[h][w - 1] = True
        dq.append([h, w - 1, l + 1])
    if len(dq) == 0:
        break

if hw_len == -1:
    print(-1)
else:
    hnum = 0
    for v in s:
        hnum += v.count(".")
    print(hnum - hw_len)