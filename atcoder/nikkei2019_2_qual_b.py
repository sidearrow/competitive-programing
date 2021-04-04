split_int_input = lambda: [int(v) for v in input().split()]
N = int(input())
D = split_int_input()

if D[0] != 0:
    print(0)
    exit()

max_d = max(D)
a = [0] * (max_d + 1)
for d in D:
    a[d] += 1

ans = 1
mod = 998244353
b = True
for i in range(1, max_d + 1):
    if a[i] == 0:
        b = False
        break
    ans *= (a[i - 1] ** a[i]) % mod
    ans %= mod

if not b or a[0] > 1:
    print(0)
else:
    print(ans)