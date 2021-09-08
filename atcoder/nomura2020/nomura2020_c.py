split_int_input = lambda: [int(v) for v in input().split()]

N = int(input())
A = split_int_input()
if N == 0:
    if A[0] == 1:
        print(1)
    else:
        print(-1)
    exit()
if A[0] != 0:
    print(-1)
    exit()

a_sum = sum(A)
tmp = 1
ans = 1
for i in range(N):
    a = A[i + 1]
    nxt = tmp * 2 - a
    if nxt < 0:
        print(-1)
        exit()
    a_sum -= a
    b = min(nxt, a_sum)
    ans += b + a
    tmp = b

print(ans)