import math
import sys

readline = sys.stdin.readline
readline_split_int = lambda: [int(v) for v in readline().split()]

a, b, x = readline_split_int()

if a * a * b / 2 > x:
    c = (x / a) * 2 / b
    ans = math.degrees(math.atan(b / c))
    print(ans)
else:
    c = ((x / a) - (a * b / 2)) * 2 / a
    if b - c == 0:
        print(0)
    else:
        ans = 90 - math.degrees(math.atan(a / (b - c)))
        print(ans)
