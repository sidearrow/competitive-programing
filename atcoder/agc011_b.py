split_int_input = lambda: [int(v) for v in input().split()]
N = int(input())
A = split_int_input()

A = sorted(A)
sum_a = []
tmp = 0
for a in A:
    tmp += a
    sum_a.append(tmp)

ans = 1
for i in range(N - 2, -1, -1):
    if sum_a[i] * 2 < A[i + 1]:
        break
    ans += 1

print(ans)
