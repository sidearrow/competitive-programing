# 12 桁の素数: 200560490131


def prime_facotrize(n):
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
