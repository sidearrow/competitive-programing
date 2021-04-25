N = int(input())

n = N
ans = N
f = 2
while f * f <= N:
    if n % f == 0:
        n //= f
        ans = ans // f * (f - 1)
        while n % f == 0:
            n //= f
    else:
        f += 1
if n != 1:
    ans = ans // n * (n - 1)

print(ans)
