N = int(input())

res = False
tmp = 0
for i in range(N):
    D1, D2 = map(int, input().split())
    if D1 == D2:
        tmp += 1
    else:
        tmp = 0
    if tmp == 3:
        res = True

if res is True:
    print("Yes")
else:
    print("No")
