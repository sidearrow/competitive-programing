import math

split_int_input = lambda: [int(v) for v in input().split()]
A, B = split_int_input()

ans = 1
for i in range(2, B + 1):
    tmp = math.floor(B / i)
    if A <= i * (tmp - 1) <= B and A <= i * tmp <= B:
        ans = i

print(ans)