import math

split_int_input = lambda: [int(v) for v in input().split()]

A, B, C = split_int_input()

abc_gcd = math.gcd(math.gcd(A, B), C)
ans = A // abc_gcd + B // abc_gcd + C // abc_gcd - 3

print(ans)