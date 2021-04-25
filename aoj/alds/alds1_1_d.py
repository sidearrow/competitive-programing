N = int(input())

mn = 10 ** 9 + 10
ans = -1 * (10 ** 9 + 10)
for i in range(N):
    r = int(input())
    if i > 0:
        ans = max(ans, r - mn)
    mn = min(mn, r)

print(ans)
