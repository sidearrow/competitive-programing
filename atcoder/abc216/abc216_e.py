from collections import deque

input_split_int = lambda: [int(v) for v in input().split()]

N, K = input_split_int()
A = input_split_int()
A = deque(sorted(A))

k = K
tmp = 0
ans = 0
while k > 0 and len(A) > 0:
    a = A.pop()
    diff = a
    tmp += 1
    if len(A) > 0:
        diff -= A[-1]
    if k >= diff * tmp:
        ans += ((a * 2 - diff + 1) * diff // 2) * tmp
    else:
        d, m = divmod(k, tmp)
        ans += (((a * 2 - d + 1)) * d // 2) * tmp
        ans += (a - d) * m
    k -= diff * tmp

print(ans)