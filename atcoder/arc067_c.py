N = int(input())


def prime_factorize(n):
    res = []
    while n % 2 == 0:
        res.append(2)
        n //= 2
    a = 3
    while a * a <= n:
        if n % a == 0:
            res.append(a)
            n //= a
        else:
            a += 2
    if n != 1:
        res.append(n)
    return res


a = [0] * (N + 1)
for i in range(2, N + 1):
    pfs = prime_factorize(i)
    for pf in pfs:
        a[pf] += 1

ans = 1
mod = 10 ** 9 + 7
for b in a[2:]:
    ans *= b + 1
    ans %= mod

print(ans)