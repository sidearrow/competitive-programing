split_int_input = lambda: [int(v) for v in input().split()]

a, b, x = split_int_input()
left = a // x + 1
right = b // x

ans = right - left + 1
if a % x == 0:
    ans += 1

print(ans)