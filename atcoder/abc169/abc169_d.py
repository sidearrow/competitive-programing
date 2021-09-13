from collections import Counter


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
n_pf_counter = Counter(prime_factorize(N))

ans = 0
for v in n_pf_counter.values():
    tmp = 1
    v -= tmp
    while v >= 0:
        ans += 1
        tmp += 1
        v -= tmp

print(ans)
