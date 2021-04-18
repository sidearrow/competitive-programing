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


split_int_input = lambda: [int(v) for v in input().split()]

N = int(input())
A = split_int_input()

if max(A) == 1:
    print("pairwise coprime")
    exit()

d = {}
for a in A:
    for v in prime_facotrize(a):
        if v in d:
            d[v] += 1
        else:
            d[v] = 1

mx = max(d.values())
if mx == 1:
    print("pairwise coprime")
elif mx < N:
    print("setwise coprime")
else:
    print("not coprime")