from collections import Counter

split_int_input = lambda: [int(v) for v in input().split()]
N = int(input())
A = split_int_input()

tmp = 0
a_sum_list = [0]
for a in A:
    tmp += a
    a_sum_list.append(tmp)

c = Counter(a_sum_list)
ans = 0
for v in c.values():
    if v >= 2:
        ans += v * (v - 1) // 2
print(ans)
