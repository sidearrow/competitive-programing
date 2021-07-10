import sys

readline = sys.stdin.readline
split_int_readline = lambda: [int(v) for v in readline().split()]

H, W = split_int_readline()
A = [split_int_readline() for _ in range(H)]
B = [split_int_readline() for _ in range(H)]

ans = 0
for h in range(H - 1):
    for w in range(W - 1):
        diff = B[h][w] - A[h][w]
        for _h, _w in [(0, 0), (0, 1), (1, 0), (1, 1)]:
            _h += h
            _w += w
            A[_h][_w] += diff
        ans += abs(diff)

for h in range(H):
    for w in range(W):
        if A[h][w] != B[h][w]:
            print("No")
            exit()

print("Yes")
print(ans)