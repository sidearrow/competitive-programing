split_int_input = lambda: [int(v) for v in input().split()]

N, K = split_int_input()
W = [int(input()) for _ in range(N)]


def judge(n):
    cnt = 1
    tmp = 0
    for w in W:
        if w > n:
            return False
        if tmp + w <= n:
            tmp += w
        else:
            cnt += 1
            if cnt > K:
                return False
            tmp = w
    return True


l = 0
r = sum(W)
while r - l > 1:
    mid = (l + r) // 2
    if judge(mid):
        r = mid
    else:
        l = mid

print(r)