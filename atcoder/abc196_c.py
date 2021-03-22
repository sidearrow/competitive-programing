N = int(input())

res = 0
for i in range(1, 10 ** 7):
    tmp = int(str(i) * 2)
    if tmp > N:
        break
    res += 1

print(res)