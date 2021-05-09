from itertools import permutations

split_int_input = lambda: [int(v) for v in input().split()]

N = int(input())
A = [split_int_input() for _ in range(N)]
M = int(input())
B = [set() for _ in range(N)]
for _ in range(M):
    x, y = split_int_input()
    B[x - 1].add(y - 1)
    B[y - 1].add(x - 1)

ans = float("inf")
for per in permutations(range(N), N):
    valid = True
    tmp_ans = 0
    prev = None
    for i, a in enumerate(per):
        if i > 0 and prev in B[a]:
            valid = False
            break
        tmp_ans += A[a][i]
        prev = a
    if valid:
        ans = min(ans, tmp_ans)

print(-1 if ans == float("inf") else ans)