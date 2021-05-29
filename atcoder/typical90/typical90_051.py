import bisect

split_int_input = lambda: [int(v) for v in input().split()]

N, K, P = split_int_input()
A = split_int_input()

AA = A[: N // 2]
AB = A[N // 2 :]

memo = []
for a in [AA, AB]:
    l = len(a)
    memo.append([[] for _ in range(l + 1)])
    for bit in range(1 << l):
        tmp = 0
        cnt = 0
        for i in range(l):
            if bit >> i & 1:
                tmp += a[i]
                cnt += 1
        memo[-1][cnt].append(tmp)
    for i in range(l + 1):
        memo[-1][i] = sorted(memo[-1][i])

ans = 0
for i, a in enumerate(memo[0]):
    if K - i >= len(memo[1]) or K - i < 0:
        continue
    for b in a:
        n = bisect.bisect_right(memo[1][K - i], P - b)
        ans += n

print(ans)