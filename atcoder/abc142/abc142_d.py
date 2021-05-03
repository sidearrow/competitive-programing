split_int_input = lambda: [int(v) for v in input().split()]
A, B = split_int_input()


def prime_facotrize(n):
    res = set()
    while n % 2 == 0:
        res.add(2)
        n //= 2
    a = 3
    while a * a <= n:
        if n % a == 0:
            res.add(a)
            n //= a
        else:
            a += 2
    if n != 1:
        res.add(n)
    return res


a = prime_facotrize(A)
b = prime_facotrize(B)

print(len(a & b) + 1)