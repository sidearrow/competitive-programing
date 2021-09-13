X = int(input())

memo = {0: 0}

a = 1
prev = 0
while 1:
    a5 = a ** 5
    b5 = a5 - X
    is_mi = False
    if b5 < 0:
        b5 *= -1
        is_mi = True
    if b5 in memo:
        b = -1 * memo[b5] if is_mi else memo[b5]
        print(a, b)
        exit()
    memo[a5] = a
    a += 1
