H, W = [int(v) for v in input().split()]
S = []

for _ in range(H):
    S.append(input())

res = 0
for h in range(1, H):
    prev = False
    for w in range(1, W):
        s1 = S[h][w]
        s2 = S[h - 1][w]
        if s1 != s2:
            prev = True
        else:
            if prev:
                res += 1
            prev = False

for w in range(1, W):
    prev = False
    for h in range(1, H):
        s1 = S[h][w]
        s2 = S[h][w - 1]
        if s1 != s2:
            prev = True
        else:
            if prev:
                res += 1
            prev = False

print(res)