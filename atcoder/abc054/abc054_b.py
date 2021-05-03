split_int_input = lambda: [int(v) for v in input().split()]
N, M = split_int_input()
A = [input() for _ in range(N)]
B = [input() for _ in range(M)]


def check(x, y):
    for i in range(M):
        if A[y + i][x : x + M] != B[i]:
            return False
    return True


for y in range(N - M + 1):
    for x in range(N - M + 1):
        if check(x, y):
            print("Yes")
            exit()
print("No")