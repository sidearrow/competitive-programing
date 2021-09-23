from collections import deque

input_split_int = lambda: [int(v) for v in input().split()]

N, S = input_split_int()
AB = [input_split_int() for _ in range(N)]

memo = [set() for _ in range(S + 1)]
memo[0].add(0)
for i in range(N):
    a, b = AB[i]
    for j in range(S, -1, -1):
        if (j - a >= 0 and i in memo[j - a]) or (j - b >= 0 and i in memo[j - b]):
            memo[j].add(i + 1)

ans = deque()


def dfs(i, s):
    if i == 0 and s == 0:
        print("".join(ans))
        exit()
    a, b = AB[i - 1]
    if s - a >= 0 and (i - 1) in memo[s - a]:
        ans.appendleft("A")
        dfs(i - 1, s - a)
        ans.popleft("A")
    if s - b >= 0 and (i - 1) in memo[s - b]:
        ans.appendleft("B")
        dfs(i - 1, s - b)
        ans.popleft("B")


if N in memo[S]:
    dfs(N, S)
else:
    print("Impossible")