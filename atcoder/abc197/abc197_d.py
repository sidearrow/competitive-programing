import math

N = int(input())
x1, y1 = [int(v) for v in input().split()]
x2, y2 = [int(v) for v in input().split()]

xc, yc = (x1 + x2) / 2, (y1 + y2) / 2
rad = math.radians(360 / N)
x3 = math.cos(rad) * (x1 - xc) - math.sin(rad) * (y1 - yc) + xc
y3 = math.sin(rad) * (x1 - xc) + math.cos(rad) * (y1 - yc) + yc
print(x3, y3)