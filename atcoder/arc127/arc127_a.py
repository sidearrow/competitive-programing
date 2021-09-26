N = input()
L = len(N)
NINT = int(N)


def count(dig, num1):
    l = int("1" * num1 + "0" * (dig - num1))
    r = int("1" * (num1 - 1) + "2" + "0" * (dig - num1))
    return max(min(r, NINT + 1) - l, 0)


ans = 0
for i in range(1, L + 1):
    for j in range(1, i + 1):
        ans += count(i, j)

print(ans)
