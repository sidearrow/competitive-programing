split_int_input = lambda: [int(v) for v in input().split()]
A, B = split_int_input()

e = []
asum = 0
for i in range(1, A + 1):
    asum += i
    e.append(i)

f = []
bsum = 0
for i in range(1, B + 1):
    i = -i
    bsum += i
    f.append(i)

if asum > abs(bsum):
    f[-1] -= asum - abs(bsum)
if asum < abs(bsum):
    e[-1] += abs(bsum) - asum

ans = e + f
print(*ans)
