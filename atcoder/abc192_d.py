def change_base_num(num: str, base_num: int):
    res = 0
    for v in num:
        res *= base_num
        res += int(v)
    return res


def solve(x: str, m: int):
    l = 2
    r = 10 ** 19
    while r - l > 1:
        mid = (l + r) // 2
        xn = change_base_num(x, mid)
        if xn <= m:
            l = mid
        else:
            r = mid
    return l


X = input().strip()
M = int(input())

if len(X) == 1:
    if int(X) <= M:
        print(1)
    else:
        print(0)
else:
    max_x = int(max(X))
    res = solve(X, M) - max_x
    print(res if res > 0 else 0)