import math

print(math.degrees(math.atan(2 / 1)))
print(math.degrees(math.atan(0)))
print(math.degrees(math.atan(1)))
print(math.degrees(math.atan(0)))

print(math.tan(math.radians(225)))


def tan_wrap(x, y):
    return math.degrees(math.atan2(y, x))


print(tan_wrap(1, -1))