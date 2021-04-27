split_int_input = lambda: [int(v) for v in input().split()]

N = int(input())
A = split_int_input()
B = split_int_input()

A = sorted(A)
B = sorted(B)
ans = 0
for a, b in zip(A, B):
    ans += abs(a - b)

print(ans)
