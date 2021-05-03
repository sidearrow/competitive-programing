import math
from decimal import Decimal

X, Y, R = [Decimal(v) for v in input().split()]

ymx = math.floor(Y + R)
ymn = math.ceil(Y - R)

r2 = R ** 2
res = 0
for y in range(ymn, ymx + 1):
    x = (r2 - (Y - y) ** 2).sqrt()
    xmx = math.floor(X + x)
    xmn = math.ceil(X - x)
    res += xmx - xmn + 1

print(res)