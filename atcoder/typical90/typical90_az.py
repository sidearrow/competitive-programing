split_int_input = lambda: [int(v) for v in input().split()]

N = int(input())
ans = 1
mod = 10 ** 9 + 7
for _ in range(N):
    A = split_int_input()
    ans = ans * sum(A) % mod
print(ans)