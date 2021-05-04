split_int_input = lambda: [int(v) for v in input().split()]
X, Y, Z = split_int_input()

ans = 0
while 1:
    if ans / Z >= Y / X:
        break
    ans += 1

print(ans - 1)