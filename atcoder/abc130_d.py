from collections import deque

split_int_input = lambda: [int(v) for v in input().split()]
N, K = split_int_input()
a = split_int_input()

ans = 0
l = 0
r = 0
tmp_sum = a[0]
while 1:
    if tmp_sum >= K:
        ans += N - r
        tmp_sum -= a[l]
        if l == N - 1:
            break
        l += 1
    else:
        if r == N - 1:
            break
        r += 1
        tmp_sum += a[r]

print(ans)