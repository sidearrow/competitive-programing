split_int_input = lambda: [int(v) for v in input().split()]

N, K = split_int_input()
A = split_int_input()
B = split_int_input()

diff = 0
for a, b in zip(A, B):
    diff += abs(a - b)

if K < diff:
    print("No")
else:
    if K % 2 == diff % 2:
        print("Yes")
    else:
        print("No")