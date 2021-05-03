from math import sqrt


def div(n):
    res = []
    for i in range(1, int(sqrt(n)) + 1):
        if n % i == 0:
            res.append(i)
            if i ** 2 != n:
                res.append(n // i)
    return res


N = int(input())

ans = [1]
for i in range(2, N + 1):
    d = div(i)
    mx = 0
    for v in d:
        if v == i:
            continue
        mx = max(mx, ans[v - 1])
    ans.append(mx + 1)

print(*ans)
