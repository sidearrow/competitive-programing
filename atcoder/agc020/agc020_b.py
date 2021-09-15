import math

input_split_int = lambda: [int(v) for v in input().split()]

K = int(input())
A = input_split_int()

l = r = 2
for a in reversed(A):
    l = math.ceil(l / a) * a
    r = math.floor(r / a) * a + a - 1
    print(l, r)
    if l > r:
        print(-1)
        exit()

print(l, r)