import math

split_int_input = lambda: [int(v) for v in input().split()]

N = int(input())
A = split_int_input()

ans = A[0]
for a in A[1:]:
    ans = ans // math.gcd(ans, a) * a

print(ans)