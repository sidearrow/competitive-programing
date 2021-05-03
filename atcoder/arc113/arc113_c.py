S = input()

a = ""
ans = 0
cnt = 0
for i in range(1, len(S)):
    if a == S[i]:
        continue
    ans += cnt
    if S[i - 1] == S[i]:
        a = S[i]
        cnt += 1

print(ans)