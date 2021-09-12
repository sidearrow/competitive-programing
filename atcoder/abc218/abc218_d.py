from collections import defaultdict

split_int_input = lambda: [int(v) for v in input().split()]

N = int(input())
X = defaultdict(set)
Y = defaultdict(set)
XY = []
for _ in range(N):
    x, y = split_int_input()
    X[x].add(y)
    Y[y].add(x)
    XY.append([x, y])
XY.sort(key=lambda v: (v[0], v[1]))

ans = 0
for i in range(N):
    x1, y1 = XY[i]
    for j in range(i + 1, N):
        x2, y2 = XY[j]
        if (
            x1 != x2
            and y1 != y2
            and y2 in X[x1]
            and y1 in X[x2]
            and x1 < x2
            and y1 < y2
        ):
            ans += 1
print(ans)