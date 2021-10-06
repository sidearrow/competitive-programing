S = input()
L = len(S)

diffnum = 0
for i in range(L // 2):
    if S[i] != S[-(i + 1)]:
        diffnum += 1
ans = 25 * L
if diffnum == 0 and L % 2:
    ans -= 25
if diffnum == 1:
    ans -= 2
print(ans)