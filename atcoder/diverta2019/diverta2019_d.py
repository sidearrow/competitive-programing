N = int(input())

ans = 0
i = 1
while 1:
    if i * (i + 1) + i > N:
        break
    if (N - i) % i == 0:
        a = (N - i) // i
        ans += (N - i) // i
    i += 1

print(ans)