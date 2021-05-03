split_int_input = lambda: [int(v) for v in input().split()]
N = int(input())
A = []
for _ in range(N):
    n = int(input())
    tmp = []
    for _ in range(n):
        x, y = split_int_input()
        tmp.append([x - 1, y])
    A.append(tmp)

ans = 0
for bit in range(1 << N):
    ok = True
    for i in range(N):
        if bit >> i & 1:
            for a in A[i]:
                if bit >> a[0] & 1 != a[1]:
                    ok = False
                    break
    if ok:
        ans = max(ans, bin(bit).count("1"))

print(ans)