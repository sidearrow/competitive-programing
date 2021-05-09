split_int_input = lambda: [int(v) for v in input().split()]

N, K = split_int_input()
for _ in range(K):
    if N % 200 == 0:
        N //= 200
    else:
        N = N * 1000 + 200

print(N)