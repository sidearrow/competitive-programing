split_int_input = lambda: [int(v) for v in input().split()]

N = int(input())
A = []
for i in range(3):
    tmp = [0] * 46
    for v in split_int_input():
        tmp[v % 46] += 1
    A.append(tmp)

ans = 0
for a in range(46):
    for b in range(46):
        for c in range(46):
            if (a + b + c) % 46 == 0:
                ans += A[0][a] * A[1][b] * A[2][c]

print(ans)