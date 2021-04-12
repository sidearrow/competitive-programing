import math

split_int_input = lambda: [int(v) for v in input().split()]
R, X, Y = split_int_input()
xy = (X ** 2 + Y ** 2) ** 0.5
ans = xy / R
if ans < 1:
    print(2)
else:
    print(math.ceil(ans))