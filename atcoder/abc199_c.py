split_int_input = lambda: [int(v) for v in input().split()]

N = int(input())
S = list(input())
Q = int(input())

is_reverse = False
for _ in range(Q):
    t, a, b = split_int_input()
    a -= 1
    b -= 1
    if is_reverse:
        a = a + N if a < N else a - N
        b = b + N if b < N else b - N
    if t == 1:
        S[a], S[b] = S[b], S[a]
    else:
        is_reverse = not is_reverse

if is_reverse:
    print("".join(S[N:]) + "".join(S[:N]))
else:
    print("".join(S))
