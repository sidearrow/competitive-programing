N = int(input())

ans = 10 ** 18
tmp = 1
for b in range(200):
    if tmp > N:
        break
    a = N // tmp
    c = N % tmp
    ans = min(ans, a + b + c)
    tmp *= 2

print(ans)