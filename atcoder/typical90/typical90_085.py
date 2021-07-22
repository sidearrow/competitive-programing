def factorize(n):
    res = []
    for i in range(1, int(n ** 0.5) + 1):
        if n % i == 0:
            res.append(i)
            j = n // i
            if i != j:
                res.append(j)
    return res


K = int(input())
divs = sorted(factorize(K))
dn = len(divs)

ans = 0
for i in range(dn):
    for j in range(i, dn):
        a, b = divs[i], divs[j]
        if K % (a * b) == 0:
            c = K // (a * b)
            if b <= c:
                ans += 1

print(ans)
