split_int_input = lambda: [int(v) for v in input().split()]
X, Y = split_int_input()


def comb(n, r, mod):
    r = min(r, n - r)
    res = 1
    for i in range(r):
        res = res * (n - i) * pow(i + 1, mod - 2, mod) % mod
    return res


if (X + Y) % 3 != 0:
    print(0)
    exit()
if 2 * X < Y or 2 * Y < X:
    print(0)
    exit()
n = (X + Y) // 3
r = X - n
ans = comb(n, r, 10 ** 9 + 7)
print(ans)