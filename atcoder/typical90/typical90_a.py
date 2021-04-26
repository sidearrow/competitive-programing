split_int_input = lambda: [int(v) for v in input().split()]

N, L = split_int_input()
K = int(input())
A = split_int_input()


def check(n):
    prev = 0
    cnt = 0
    for a in A:
        if a - prev >= n:
            prev = a
            cnt += 1
            if cnt == K:
                break
    if cnt < K or L - prev < n:
        return False
    else:
        return True


l = 1
r = L
while r - l > 1:
    mid = (l + r) // 2
    if check(mid):
        l = mid
    else:
        r = mid

print(l)