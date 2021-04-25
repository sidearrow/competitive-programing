from math import sqrt


def is_prime(n):
    mx = int(sqrt(n))
    for i in range(2, mx + 1):
        if n % i == 0:
            return False
    return True


N = int(input())
ans = 0
for _ in range(N):
    n = int(input())
    if is_prime(n):
        ans += 1

print(ans)