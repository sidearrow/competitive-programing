# from math import gcd

split_int_input = lambda: [int(v) for v in input().split()]


def gcd(a, b):
    if b > a:
        a, b = b, a
    div = a % b
    if div == 0:
        return b
    return gcd(b, div)


x, y = split_int_input()
print(gcd(x, y))