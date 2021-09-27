K = int(input())
A, B = input().split()


def conv(n):
    res = 0
    for v in n:
        res *= K
        res += int(v)
    return res


a = conv(A)
b = conv(B)

print(a * b)