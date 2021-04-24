split_int_input = lambda: [int(v) for v in input().split()]
N = int(input())
F = []
for _ in range(N):
    tmp = 0
    for v in input().split():
        tmp *= 2
        tmp += int(v)
    F.append(tmp)
P = [split_int_input() for _ in range(N)]

ans = -(10 ** 9)
for bit in range(1, 2 ** 10):
    tmp = 0
    for f, p in zip(F, P):
        cnt = bin(bit & f).count("1")
        tmp += p[cnt]
    ans = max(ans, tmp)

print(ans)