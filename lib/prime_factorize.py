def prime_facotrize(n):
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


assert sorted(prime_facotrize(13)) == [13]
assert sorted(prime_facotrize(2 * 2 * 2 * 3 * 3 * 7)) == [2, 2, 2, 3, 3, 7]