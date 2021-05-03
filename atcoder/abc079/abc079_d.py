split_int_input = lambda: [int(v) for v in input().split()]
H, W = split_int_input()
c = []
A = []
for _ in range(10):
    c.append(split_int_input())
for i in range(H):
    A.append(split_int_input())
a = [c[i][1] for i in range(10)]
while 1:
    cont = False
    for j in range(10):
        for k in range(10):
            if a[j] > a[k] + c[j][k]:
                cont = True
                a[j] = a[k] + c[j][k]
    if not cont:
        break
ans = 0
for row in A:
    for v in row:
        if v > -1:
            ans += a[v]
print(ans)