N = int(input())

ans = N // 11 * 2
N %= 11
if 1 <= N <= 6:
    ans += 1
elif 7 <= N:
    ans += 2

print(ans)