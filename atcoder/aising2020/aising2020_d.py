N = int(input())
X = input()


def f(a):
    cnt = 0
    while a > 0:
        cnt += 1
        a %= bin(a).count("1")
    return cnt


x_popcount = X.count("1")
modmemo = [[0] * 2 for _ in range(N)]
if x_popcount != 1:
    modmemo[0][0] = 1 % (x_popcount - 1)
modmemo[0][1] = 1 % (x_popcount + 1)
for i in range(1, N):
    if x_popcount != 1:
        modmemo[i][0] = modmemo[i - 1][0] * 2 % (x_popcount - 1)
    modmemo[i][1] = modmemo[i - 1][1] * 2 % (x_popcount + 1)

modx = [0, 0]
for i in range(N):
    if X[N - i - 1] == "1":
        if x_popcount != 1:
            modx[0] = (modx[0] + modmemo[i][0]) % (x_popcount - 1)
        modx[1] = (modx[1] + modmemo[i][1]) % (x_popcount + 1)

ans = []
for i in range(N):
    if X[N - i - 1] == "1":
        if x_popcount != 1:
            tmp = (modx[0] - modmemo[i][0]) % (x_popcount - 1)
        else:
            ans.append(0)
            continue
    else:
        tmp = (modx[1] + modmemo[i][1]) % (x_popcount + 1)
    ans.append(f(tmp) + 1)

print(*reversed(ans), sep="\n")
