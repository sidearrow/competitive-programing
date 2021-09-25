K = int(input())

ans = 0
for a in range(1, 100):
    for b in range(a, int(K // a) + 1):
        cmax = int(K // (a * b))
        if b > cmax:
            break
        for c in range(b, cmax + 1):
            if a == b and b == c:
                ans += 1
                continue
            if a == b or b == c or a == c:
                ans += 3
                continue
            ans += 6

print(ans)