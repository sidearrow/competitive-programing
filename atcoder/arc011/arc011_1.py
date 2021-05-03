split_int_input = lambda: [int(v) for v in input().split()]

m, n, N = split_int_input()

ans = N
while 1:
    tmp = N // m * n
    if tmp == 0:
        break
    ans += tmp
    N = tmp + (N % m)

print(ans)