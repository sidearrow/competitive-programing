split_int_input = lambda: [int(v) for v in input().split()]
N, K = split_int_input()

ans = 0
l = 0
r = 0
mod = 10 ** 9 + 7
for i in range(N + 1):
    l += i
    r += N - i
    if i + 1 >= K:
        ans += r - l + 1
        ans %= mod
print(ans)
