def prime_factorize(n):
    res = []
    while n % 2 == 0:
        res.append(2)
        n //= 2
    i = 3
    while i ** 2 <= n:
        if n % i == 0:
            res.append(i)
            n //= i
        else:
            i += 2
    if n != 1:
        res.append(n)
    return res


N = int(input())
i = len(prime_factorize(N))
if i == 1:
    print(0)
else:
    print(len(bin(i - 1)) - 2)