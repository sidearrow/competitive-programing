split_int_input = lambda: [int(v) for v in input().split()]
A, B, C = split_int_input()

if A ** 2 + B ** 2 < C ** 2:
    print("Yes")
else:
    print("No")