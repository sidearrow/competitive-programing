split_int_input = lambda: [int(v) for v in input().split()]

N, Q = split_int_input()
A = split_int_input()

a = 0
l = len(A)
for _ in range(Q):
    t, x, y = split_int_input()
    x, y = x - 1, y - 1
    if t == 1:
        x = (x - a) % l
        y = (y - a) % l
        A[x], A[y] = A[y], A[x]
    elif t == 2:
        a += 1
    elif t == 3:
        print(A[(x - a) % l])
