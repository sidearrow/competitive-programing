from bisect import bisect_left, bisect_right


a = [3, 5, 7, 9]

print(bisect_left(a, 2))  # 0
print(bisect_right(a, 2))  # 0

print(bisect_left(a, 3))  # 0
print(bisect_right(a, 3))  # 1

print(bisect_left(a, 4))  # 1
print(bisect_right(a, 4))  # 1

print(bisect_left(a, 9))  # 3
print(bisect_right(a, 9))  # 4

print(bisect_left(a, 10))  # 4
print(bisect_right(a, 10))  # 4