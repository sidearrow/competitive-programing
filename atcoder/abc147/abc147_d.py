split_int_input = lambda: [int(v) for v in input().split()]

N = int(input())
A = split_int_input()
A = list(reversed(A))

memo = [0] * 61
ans = 0
mod = 10 ** 9 + 7
for i, a in enumerate(A):
    tmp = 1
    for j in range(61):
        if a & 1:
            if i > 0:
                ans = (ans + (i - memo[j]) * tmp) % mod
            memo[j] += 1
        else:
            if i > 0:
                ans = (ans + memo[j] * tmp) % mod
        a >>= 1
        tmp = tmp * 2 % mod

print(ans)
