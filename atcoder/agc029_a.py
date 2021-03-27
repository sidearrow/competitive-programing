S = input()
l = len(S)

bmax = l - 1
ans = 0
for i in range(l):
    idx = l - 1 - i
    if S[idx] == "B":
        ans += bmax - idx
        bmax -= 1

print(ans)