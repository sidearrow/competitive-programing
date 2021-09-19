input_split_int = lambda: [int(v) for v in input().split()]

N = int(input())
X, Y = input_split_int()
AB = [input_split_int() for _ in range(N)]

memo = [[N + 1] * (Y + 1) for _ in range(X + 1)]
memo[0][0] = 0
for i in range(N):
    a, b = AB[i]
    for x in range(X, -1, -1):
        for y in range(Y, -1, -1):
            _x = min(X, x + a)
            _y = min(Y, y + b)
            memo[_x][_y] = min(memo[x][y] + 1, memo[_x][_y])
ans = memo[X][Y]
print(-1 if ans > N else ans)
