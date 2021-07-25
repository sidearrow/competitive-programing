split_int_input = lambda: [int(v) for v in input().split()]

A, B = split_int_input()

c = (A - B) / 3 + B
print(c)
