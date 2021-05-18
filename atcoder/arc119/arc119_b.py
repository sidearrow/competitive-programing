N = int(input())
S = input()
T = input()

a0 = 0
a1 = 0
ans = 0
for s, t in zip(S, T):
    if s == t:
        if s == "0" and (a0 + a1) > 0:
            ans += 1
        continue
    if s == "0":
        if a1 > 0:
            a1 -= 1
            ans += 1
        else:
            a0 += 1
    else:
        if a0 > 0:
            a0 -= 1
            ans += 1
        else:
            a1 += 1

if a0 == 0 and a1 == 0:
    print(ans)
else:
    print(-1)