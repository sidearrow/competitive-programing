split_int_input = lambda: [int(v) for v in input().split()]

N = int(input())
A = []
for i in range(N):
    x, y = split_int_input()
    A.append([i, x, y])

AX = sorted(A, key=lambda v: v[1], reverse=True)[:2]
AY = sorted(A, key=lambda v: v[2], reverse=True)[:2]

memo = set()
memoidx = set()
for a in [AX, AY]:
    for i, x, y in a:
        memoidx.add(i)
        memo.add((i, x, y))

ans = [-1, -1]
for i, x, y in A:
    for j, _x, _y in memo:
        if i == j or (i in memoidx and i > j):
            continue
        d = max(abs(x - _x), abs(y - _y))
        if d >= ans[0]:
            ans[1] = ans[0]
            ans[0] = d
        elif d >= ans[1]:
            ans[1] = d

print(ans[1])