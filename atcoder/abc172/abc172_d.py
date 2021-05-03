N = int(input())
ans = 0
for i in range(1, N + 1):
    a = N // i
    ans += (i + i * a) * a // 2
print(ans)