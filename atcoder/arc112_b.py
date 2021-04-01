import sys

split_int_input = lambda: [int(v) for v in input().split()]
B, C = split_int_input()

c1 = C
if B > 0:
    c1 -= 1
mn = -abs(B) - c1 // 2
mx = -mn
if c1 % 2 == 0:
    mx = max(mx - 1, B)

c2 = C
if B < 0:
    c2 -= 1
mx2 = abs(B) - c2 // 2
mn2 = -mx2
if c2 % 2 == 0:
    mn2 -= 1

ans = mx - mn + 1
if mx2 > 0:
    ans -= mx2 - mn2 - 1

print(ans)