from bisect import bisect_left

split_int_input = lambda: [int(v) for v in input().split()]

N, M = split_int_input()
A = sorted(split_int_input())
B = sorted(split_int_input())

ans = float("inf")
for a in A:
    res = bisect_left(B, a)
    idxs = []
    if res != 0:
        idxs.append(res - 1)
    if res != M:
        idxs.append(res)
    for idx in idxs:
        ans = min(ans, abs(a - B[idx]))

print(ans)
