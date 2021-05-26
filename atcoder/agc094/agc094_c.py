N = int(input())
A = [int(input()) for _ in range(N)]

if A[0] > 0:
    print(-1)
    exit()

ans = 0
for i in range(1, N):
    l, r = A[i - 1], A[i]
    if l < r:
        if r - l > 1:
            print(-1)
            exit()
        else:
            ans += 1
    else:
        ans += r

print(ans)