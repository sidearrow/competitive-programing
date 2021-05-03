split_int_input = lambda: [int(v) for v in input().split()]
N = int(input())
A = split_int_input()

cnt = 0
mn = 10 ** 9 + 10
ans = 0
for a in A:
    if a < 0:
        cnt += 1
    ans += abs(a)
    mn = min(mn, abs(a))

if cnt % 2 == 0:
    print(ans)
else:
    print(ans - mn * 2)