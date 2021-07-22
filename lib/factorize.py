def factorize(n):
    res = []
    for i in range(1, int(n ** 0.5) + 1):
        if n % i == 0:
            res.append(i)
            j = n // i
            if i != j:
                res.append(j)
    return res
