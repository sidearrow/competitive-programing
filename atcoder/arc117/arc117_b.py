split_int_input = lambda: [int(v) for v in input().split()]
N = int(input())
A = split_int_input()
A = sorted(list(set(A)))

ans = 1
prev = 0
mod = 10 ** 9 + 7
for a in A:
    ans = ans * (a - prev + 1) % mod
    prev = a

print(ans)