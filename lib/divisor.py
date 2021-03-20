def make_divisors(n):
    divisors = []
    for i in range(1, int(n ** 0.5) + 1):
        if n % i == 0:
            divisors.append(i)
            j = n // i
            if i != j:
                divisors.append(j)
    divisors.sort()
    return divisors


print(make_divisors(1000000007))
