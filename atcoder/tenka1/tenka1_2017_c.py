from itertools import combinations

N = int(input())

for a, b in combinations(range(1, 3501), 2):
    x = N * a * b
    y = 4 * a * b - N * (a + b)
    if y <= 0:
        continue
    if x % y == 0:
        print(a, b, x // y)
        exit()