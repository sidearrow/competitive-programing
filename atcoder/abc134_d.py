split_int_input = lambda: [int(v) for v in input().split()]
N = int(input())
a = [-1] + split_int_input()


def div(n):
    res = []
    for a in range(1, int(n ** 0.5) + 1):
        if n % a == 0:
            res.append(a)
            if n // a != a:
                res.append(n // a)
    return res


tmp = [0] * (N + 1)
ans = []
for i in range(N, 0, -1):
    if tmp[i] != a[i]:
        ans.append(i)
        for d in div(i):
            tmp[d] = 1 if tmp[d] == 0 else 0

print(len(ans))
if len(ans) > 0:
    print(*ans)