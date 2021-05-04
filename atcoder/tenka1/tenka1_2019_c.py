N = int(input())
S = input()

w = [0]
b = [0]
tmpw = 0
tmpb = 0
for s in S:
    if s == ".":
        tmpw += 1
    else:
        tmpb += 1
    w.append(tmpw)
    b.append(tmpb)

ans = 10 ** 6
maxw = w[-1]
for i in range(N + 1):
    ans = min(ans, b[i] + maxw - w[i])

print(ans)
