from bisect import bisect_left

N = int(input())
A = [int(v) for v in input().split()]


def get_lislen(lst):
    lis = [lst[0]]
    lislen = [0] * N
    lislen[0] = 1
    cnt = 1
    for i, a in enumerate(lst[1:], 1):
        if lis[-1] < a:
            lis.append(a)
            cnt += 1
        else:
            lis[bisect_left(lis, a)] = a
        lislen[i] = cnt
    return lislen


a = get_lislen(A)
A.reverse()
b = get_lislen(A)
b.reverse()

ans = -1
for i in range(N):
    ans = max(ans, a[i] + b[i] - 1)
print(ans)