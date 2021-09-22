def sieve_eratosthenes(n):
    primes = [False, True] * (n // 2 + 1)
    if n % 2 == 0:
        primes.pop()
    primes[1] = False
    for i in range(3, int(n ** 0.5) + 1, 2):
        if primes[i]:
            for j in range(i * i, n + 1, 2 * i):
                primes[j] = False
    primes2 = [i for i in range(n) if primes[i]]
    return primes2
