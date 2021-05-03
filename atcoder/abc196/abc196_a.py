split_int_input = lambda: [int(v) for v in input().split()]

a, b = split_int_input()
c, d = split_int_input()

res = -1000
for x in range(a, b + 1):
    for y in range(c, d + 1):
        res = max(res, x - y)

print(res)
