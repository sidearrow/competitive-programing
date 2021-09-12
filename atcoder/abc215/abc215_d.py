def prime_factorize_set(n):
    res = set()
    while n % 2 == 0:
        res.add(2)
        n //= 2
    i = 3
    while i ** 2 <= n:
        if n % i == 0:
            res.add(i)
            n //= i
        else:
            i += 2
    if n != 1:
        res.add(n)
    return res


input_split_int = lambda: [int(v) for v in input().split()]

N, M = input_split_int()
A = input_split_int()

is_multi = [False] * (M + 1)


def update_is_multi(n):
    a = n
    while a <= M:
        is_multi[a] = True
        a += n


for a in A:
    a_pf = prime_factorize_set(a)
    for b in a_pf:
        if b <= M and not is_multi[b]:
            update_is_multi(b)

ans = []
for i in range(1, M + 1):
    if not is_multi[i]:
        ans.append(i)

print(len(ans))
print(*ans, sep="\n")