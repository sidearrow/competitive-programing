from collections import Counter

split_int_input = lambda: [int(v) for v in input().split()]

N = int(input())
A = split_int_input()
B = split_int_input()
C = split_int_input()

ac = Counter(A)
cc = Counter(C)
bc = [[] for _ in range(N + 1)]
for i, b in enumerate(B, 1):
    bc[b].append(i)

ans = 0
for k, v in ac.items():
    if v == 0:
        continue
    for b in bc[k]:
        ans += v * cc[b]

print(ans)