import sys

readline = sys.stdin.readline
split_int_readline = lambda: [int(v) for v in readline().split()]

L, R = split_int_readline()
MOD = 10 ** 9 + 7

ans = 0
a = 10
b = 1
l = L
while 1:
    if l < a:
        if R < a:
            ans = (ans + ((l + R) * (R - l + 1) // 2) * b) % MOD
            break
        else:
            ans = (ans + ((l + a - 1) * (a - l) // 2) * b) % MOD
            l = a
    a *= 10
    b += 1

print(ans)