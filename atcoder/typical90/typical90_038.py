import math

split_int_input = lambda: [int(v) for v in input().split()]

A, B = split_int_input()

ans = A // math.gcd(A, B) * B
if ans > 10 ** 18:
    print("Large")
else:
    print(ans)
