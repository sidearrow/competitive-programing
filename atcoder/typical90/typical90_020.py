split_int_input = lambda: [int(v) for v in input().split()]

a, b, c = split_int_input()

if a < c ** b:
    print("Yes")
else:
    print("No")