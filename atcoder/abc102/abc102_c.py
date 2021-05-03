from statistics import median

split_int_input = lambda: [int(v) for v in input().split()]

N = int(input())
A = split_int_input()
A = [A[i] - i for i in range(N)]

meda = int(median(A))

ans = 0
for a in A:
    ans += abs(meda - a)

print(ans)