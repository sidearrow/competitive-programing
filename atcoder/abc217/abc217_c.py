split_int_input = lambda: [int(v) for v in input().split()]

N = int(input())
P = split_int_input()

q = [0] * N
for i in range(N):
    q[P[i] - 1] = i + 1

print(*q)