split_int_input = lambda: [int(v) for v in input().split()]
N, P = split_int_input()
A = split_int_input()

e = 1
o = 0
for a in A:
    if a % 2 == 0:
        e += e
        o += o
    else:
        e, o = e + o, e + o

if P % 2 == 0:
    print(e)
else:
    print(o)