N = int(input())

a = 1
tmp = 0
while 1:
    tmp += a
    if tmp >= N:
        break
    a += 1

b = tmp - N
for i in range(1, a + 1):
    if i == b:
        continue
    print(i)