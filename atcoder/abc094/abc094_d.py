from bisect import bisect_left

split_int_input = lambda: [int(v) for v in input().split()]
n = int(input())
a = split_int_input()

a = sorted(a)
mid = a[-1] / 2
b = bisect_left(a, mid)

ans = b
if b == n - 1 or a[b] - mid > mid - a[b - 1]:
    ans = b - 1
print(a[-1], a[ans])