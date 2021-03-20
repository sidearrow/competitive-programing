import sys

input = sys.stdin.readline

N, M, Q = [int(v) for v in input().split()]
WV = []
for _ in range(N):
    w, v = [int(v) for v in input().split()]
    WV.append({"w": w, "v": v})
WV.sort(key=lambda v: v["v"], reverse=True)

X = [int(v) for v in input().split()]
boxs = [{"i": i + 1, "x": x} for i, x in enumerate(X)]
boxs.sort(key=lambda v: v["x"])
q = []
for _ in range(Q):
    l, r = [int(v) for v in input().split()]
    q.append([l, r])

for l, r in q:
    _boxs = [*boxs]
    maxv = 0
    for wv in WV:
        w = wv["w"]
        v = wv["v"]
        for j, b in enumerate(_boxs):
            x = b["x"]
            i = b["i"]
            if l <= i <= r:
                continue
            if w <= x:
                maxv += v
                del _boxs[j]
                break
    print(maxv)
