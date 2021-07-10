N = int(input())
S = input()

ans = 0
add = 0
tmp = 1

for i in range(1, N):
    if S[i - 1] == S[i]:
        tmp += 1
    else:
        add += tmp
        tmp = 1
    ans += add

print(ans)