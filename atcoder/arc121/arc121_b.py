from bisect import bisect_left

split_int_input = lambda: [int(v) for v in input().split()]

N = int(input())
A = [[] for _ in range(3)]
CLR = {"R": 0, "G": 1, "B": 2}
for _ in range(N * 2):
    a, c = input().split()
    A[CLR[c]].append(int(a))

target = []
target2 = None
for a in A:
    if len(a) % 2:
        target.append(sorted(a))
    else:
        target2 = a

if len(target) == 0:
    print(0)
    exit()

ans = float("inf")
a, b = target
la = len(a)
lb = len(b)
for v in b:
    idx = bisect_left(a, v)
    if 0 <= idx < la:
        ans = min(ans, abs(v - a[idx]))
    if 0 <= idx - 1 < la:
        ans = min(ans, abs(v - a[idx - 1]))

if len(target2) == 0:
    print(ans)
    exit()

ab = []
ac = []
for i, v in enumerate(target2):
    idx = bisect_left(a, v)
    if 0 <= idx < la:
        ab.append([i, abs(v - a[idx])])
    if 0 <= idx - 1 < la:
        ab.append([i, abs(v - a[idx - 1])])
    idx = bisect_left(b, v)
    if 0 <= idx < lb:
        ac.append([i, abs(v - b[idx])])
    if 0 <= idx - 1 < lb:
        ac.append([i, abs(v - b[idx - 1])])

ab = sorted(ab, key=lambda v: v[1])[:2]
ac = sorted(ac, key=lambda v: v[1])[:2]
if ab[0][0] != ac[0][0]:
    tmp = ab[0][1] + ac[0][1]
else:
    tmp = min(ab[0][1] + ac[1][1], ab[1][1] + ac[0][1])

ans = min(ans, tmp)
print(ans)
