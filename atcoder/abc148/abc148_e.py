N = int(input())

if N % 2 == 1:
    print(0)
    exit()

ans = N // 10
a = 50
while a <= N:
    ans += N // a
    a *= 5

print(ans)