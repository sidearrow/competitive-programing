from collections import defaultdict


def prime_factorize(n):
    res = defaultdict(int)
    while n % 2 == 0:
        res[2] += 1
        n //= 2
    i = 3
    while i ** 2 <= n:
        if n % i == 0:
            res[i] += 1
            n //= i
        else:
            i += 2
    if n != 1:
        res[n] += 1
    return res


A, B = [int(v) for v in input().split()]
apf = prime_factorize(A)
bpf = prime_factorize(B)

keyset = set()
for k in apf.keys():
    keyset.add(k)
for k in bpf.keys():
    keyset.add(k)

ans = True
for k in keyset:
    if apf[k] * B != bpf[k] * A:
        ans = False
        break
print("Yes" if ans else "No")