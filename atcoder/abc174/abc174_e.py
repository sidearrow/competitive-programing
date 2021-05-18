split_int_input = lambda: [int(v) for v in input().split()]

N, K = split_int_input()
A = split_int_input()


def check(l):
    cnt = 0
    for a in A:
        cnt += a // l
        if a % l == 0:
            cnt -= 1
    return cnt <= K


l = 0
r = max(A)
while r - l > 1:
    m = (l + r) // 2
    if check(m):
        r = m
    else:
        l = m

print(r)
