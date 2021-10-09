import sys

readline = sys.stdin.readline
readline2 = lambda: [int(v) for v in readline().split()]

X, Y, Z, K = readline2()
A = readline2()
B = readline2()
C = readline2()

ab = []
for a in A:
    for b in B:
        ab.append(a + b)
ab.sort(reverse=True)
ab = ab[:K]

ans = []
for v in ab:
    for c in C:
        ans.append(v + c)
ans.sort(reverse=True)
ans = ans[:K]

for a in ans:
    print(a)