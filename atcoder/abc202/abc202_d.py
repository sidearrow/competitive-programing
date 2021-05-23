split_int_input = lambda: [int(v) for v in input().split()]

A, B, K = split_int_input()


def clc(a, b):
    res = 1
    m = min(a, b)
    for i in range(m):
        res *= a + b - i
    for i in range(1, m + 1):
        res //= i
    return res


ans = []
a, b, k = A, B, K
while 1:
    if a + b == 0:
        break
    if a == 0:
        ans.append("b")
        b -= 1
        continue
    if b == 0:
        ans.append("a")
        a -= 1
        continue
    tmp = clc(a - 1, b)
    if k > tmp:
        ans.append("b")
        k -= tmp
        b -= 1
    else:
        ans.append("a")
        a -= 1

print("".join(ans))