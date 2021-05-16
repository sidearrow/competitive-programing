split_int_input = lambda: [int(v) for v in input().split()]

A = split_int_input()
A = sorted(A)

if A[2] - A[1] == A[1] - A[0]:
    print("Yes")
else:
    print("No")