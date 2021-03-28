split_int_input = lambda: [int(v) for v in input().split()]

N, M = split_int_input()
S = []
for _ in range(M):
    s = split_int_input()
    S.append(s[1:])
P = split_int_input()

ans = 0
for bit in range(1 << N):
    tmp = [0] * M
    for i in range(N):
        if bit >> i & 1:
            for j in range(M):
                if (i + 1) in S[j]:
                    tmp[j] += 1
    tmpans = True
    for i in range(M):
        if tmp[i] % 2 != P[i]:
            tmpans = False
            break
    if tmpans:
        ans += 1

print(ans)
