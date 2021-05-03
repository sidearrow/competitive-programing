split_int_input = lambda: [int(v) for v in input().split()]
N = int(input())
A = split_int_input()

d = {}
ans = 0
for i, a in enumerate(A, 1):
    ans += d.get(i - a, 0)
    ia_sum = i + a
    if ia_sum in d:
        d[ia_sum] += 1
    else:
        d[ia_sum] = 1

print(ans)