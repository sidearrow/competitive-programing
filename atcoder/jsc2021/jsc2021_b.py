from collections import Counter

split_int_input = lambda: [int(v) for v in input().split()]
N, M = split_int_input()
A = split_int_input()
B = split_int_input()

c = Counter(A + B)
ans = []
for k, v in c.items():
    if v == 1:
        ans.append(k)

print(*sorted(ans))