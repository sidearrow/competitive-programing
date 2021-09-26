def factorize(n):
    res = []
    for i in range(1, int(n ** 0.5) + 1):
        if n % i == 0:
            res.append(i)
            j = n // i
            if i != j:
                res.append(j)
    return res


N = int(input())

n_facts = factorize(N)
n_odd_facts = [v for v in n_facts if v % 2 == 1]

ans = len(n_odd_facts) * 2
print(ans)