split_int_input = lambda: [int(v) for v in input().split()]

A, B, C = split_int_input()

memo = [[[0] * 101 for _ in range(101)] for _ in range(101)]

for a in range(99, -1, -1):
    for b in range(99, -1, -1):
        for c in range(99, -1, -1):
            sum_abc = a + b + c
            if sum_abc == 0:
                continue
            tmp = (memo[a + 1][b][c] + 1) * a / sum_abc
            tmp += (memo[a][b + 1][c] + 1) * b / sum_abc
            tmp += (memo[a][b][c + 1] + 1) * c / sum_abc
            memo[a][b][c] = tmp

print(memo[A][B][C])