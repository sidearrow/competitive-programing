input_split_int = lambda: [int(v) for v in input().split()]
N, K = input_split_int()
A = input_split_int()

l = []
for i in range(N):
    for j in range(i):
        l.append(l[-1 * i] + A[i])
    l.append(A[i])

ans = 0
max_bit_digit = len(bin(max(l))) - 2
for i in range(max_bit_digit - 1, -1, -1):
    cnt = 0
    tmp = ans + 2 ** i
    for v in l:
        if v & tmp == tmp:
            cnt += 1
    if cnt >= K:
        ans = tmp

print(ans)