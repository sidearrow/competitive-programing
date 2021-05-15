split_int_input = lambda: [int(v) for v in input().split()]

H, W, D = split_int_input()
memo = [None] * (H * W + 1)
for h in range(1, H + 1):
    a = split_int_input()
    for w, a in enumerate(a, 1):
        memo[a] = [h, w]

memo2 = [-1] * (H * W + 1)
for i in range(1, H * W + 1):
    if i - D <= 0:
        memo2[i] = 0
    else:
        h1, w1 = memo[i - D]
        h2, w2 = memo[i]
        memo2[i] = memo2[i - D] + abs(h1 - h2) + abs(w1 - w2)

Q = int(input())
for _ in range(Q):
    l, r = split_int_input()
    print(memo2[r] - memo2[l])