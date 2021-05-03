import sys

input = sys.stdin.readline

N = int(input())

min_a = None
min_b = None

la = []
lb = []
for idx in range(N):
    a, b = [int(v) for v in input().split()]
    la.append([idx, a])
    lb.append([idx, b])

la.sort(key=lambda v: v[1])
lb.sort(key=lambda v: v[1])

res = 0
if la[0][0] != lb[0][0]:
    res = max(la[0][1], lb[0][1])
else:
    p0 = la[0][1] + lb[0][1]
    p1 = max(la[0][1], lb[1][1])
    p2 = max(la[1][1], lb[0][1])
    res = min([p0, p1, p2])

print(res)
