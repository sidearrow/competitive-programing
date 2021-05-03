split_int_input = lambda: [int(v) for v in input().split()]
N = int(input())
A = split_int_input()
B = split_int_input()

s = [0] * 1010
for a, b in zip(A, B):
    for i in range(a, b + 1):
        s[i] += 1

ans = 0
for v in s:
    if v == N:
        ans += 1

print(ans)
