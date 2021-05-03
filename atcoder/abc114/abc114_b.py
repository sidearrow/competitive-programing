S = input()

ans = 1000
for i in range(len(S) - 2):
    tmp = abs(753 - int(S[i : i + 3]))
    ans = min(ans, tmp)

print(ans)