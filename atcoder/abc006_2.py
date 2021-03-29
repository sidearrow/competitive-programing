n = int(input())
MOD = 10007


a = 0
b = 0
c = 1

if n == 1:
    print(a)
elif n == 2:
    print(b)
elif n == 3:
    print(c)
else:
    for _ in range(4, n + 1):
        a, b, c = b, c, (a + b + c) % MOD
    print(c)