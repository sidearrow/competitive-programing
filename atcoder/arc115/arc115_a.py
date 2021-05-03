split_int_input = lambda: [int(v) for v in input().split()]


def zero_num(s):
    tmp = 0
    for v in s:
        if v == "0":
            tmp += 1
    return tmp


N, M = split_int_input()
a = 0
b = 0
for _ in range(N):
    s = input()
    zn = zero_num(s)
    if zn % 2 == 0:
        a += 1
    else:
        b += 1

ans = N * (N - 1) // 2
if a > 1:
    ans -= a * (a - 1) // 2
if b > 1:
    ans -= b * (b - 1) // 2

print(ans)