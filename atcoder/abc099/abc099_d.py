input2 = lambda: [int(v) for v in input().split()]


def main():
    N, C = input2()
    D = [input2() for _ in range(C)]
    E = [input2() for _ in range(N)]

    memo = [[0] * 3 for _ in range(C)]
    for i in range(N):
        for j in range(N):
            color = E[i][j] - 1
            m = (i + j + 2) % 3
            for k in range(C):
                memo[k][m] += D[color][k]

    ans = float("inf")
    for a in range(C):
        for b in range(C):
            for c in range(C):
                if a == b or a == c or b == c:
                    continue
                tmpans = memo[a][0] + memo[b][1] + memo[c][2]
                if ans > tmpans:
                    ans = tmpans

    print(ans)


main()