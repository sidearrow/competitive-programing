N = int(input())

S = [input() for _ in range(N)]
T = [input() for _ in range(N)]


def conv(a):
    res = set()
    tmp = None
    for i in range(N):
        for j in range(N):
            if tmp is None and a[i][j] == "#":
                tmp = [i, j]
            if a[i][j] == "#":
                res.add((i - tmp[0], j - tmp[1]))
    return res


def check(a, b):
    if a == b:
        print("Yes")
        exit()


s = conv(S)
t = conv(T)
check(s, t)

s = []
for w in range(N):
    tmp = []
    for h in range(N - 1, -1, -1):
        tmp.append(S[h][w])
    s.append(tmp)
check(conv(s), t)

s = []
for h in range(N - 1, -1, -1):
    tmp = []
    for w in range(N - 1, -1, -1):
        tmp.append(S[h][w])
    s.append(tmp)
check(conv(s), t)

s = []
for w in range(N - 1, -1, -1):
    tmp = []
    for h in range(N):
        tmp.append(S[h][w])
    s.append(tmp)
check(conv(s), t)

print("No")