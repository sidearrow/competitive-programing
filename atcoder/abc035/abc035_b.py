S = list(input())
T = int(input())

A = {
    "L": [-1, 0],
    "R": [1, 0],
    "U": [0, 1],
    "D": [0, -1],
}

x = y = cnt = 0
for s in S:
    if s == "?":
        cnt += 1
    else:
        _x, _y = A[s]
        x += _x
        y += _y

x = abs(x)
y = abs(y)
if T == 1:
    print(x + y + cnt)
else:
    if x + y > cnt:
        print(x + y - cnt)
    else:
        cnt -= x + y
        print(cnt % 2)