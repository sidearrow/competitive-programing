split_int_input = lambda: [int(v) for v in input().split()]
N = int(input())
A = split_int_input()
A = sorted(A)

check = True
is_odd = N % 2 == 1
for i in range(N):
    if is_odd:
        tmp = i + i % 2
    else:
        tmp = i + 1 - i % 2
    if tmp != A[i]:
        check = False
        break
if check:
    mod = 10 ** 9 + 7
    ans = 1
    for _ in range(N // 2):
        ans *= 2
        ans %= mod
    print(ans)
else:
    print(0)