split_int_input = lambda: [int(v) for v in input().split()]
N = int(input())
A = split_int_input()

ans = [0]
for i in range(N):
    tmp = (A[i] - ans[i] // 2) * 2
    ans.append(tmp)

diff = (ans[0] + ans[-1]) // 2
a = []
for i in range(N):
    b = ans[i] + diff if i % 2 == 0 else ans[i] - diff
    a.append(b)

print(*a)
