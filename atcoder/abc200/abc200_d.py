split_int_input = lambda: [int(v) for v in input().split()]

N = int(input())
A = split_int_input()

dp = [None] * 200
B = None
C = None
for i, a in enumerate(A):
    nxt = [*dp]
    if dp[a % 200] is not None:
        B = dp[a % 200]
        C = [i]
        break
    nxt[a % 200] = [i]
    is_break = False
    for j, b in enumerate(dp):
        if b is not None:
            tmp = (j + a) % 200
            if dp[tmp] is not None:
                B = dp[tmp]
                C = b + [i]
                is_break = True
            else:
                nxt[tmp] = b + [i]
    if is_break:
        break
    dp = nxt

if B is not None:
    print("Yes")
    print(len(B), *[b + 1 for b in B])
    print(len(C), *[c + 1 for c in C])
else:
    print("No")