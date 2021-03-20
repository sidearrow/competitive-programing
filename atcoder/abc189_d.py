N = int(input())
S = [input() == "AND" for _ in range(N)]

t = 1
f = 1
for s in S:
    if s:
        f = t + 2 * f
    else:
        t = 2 * t + f
print(t)
