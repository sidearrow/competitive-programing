N = int(input())


def ans(s, l):
    if len(s) == N:
        if l == 0:
            print(s)
        return
    if l < N // 2:
        ans(s + "(", l + 1)
    if l > 0:
        ans(s + ")", l - 1)


ans("", 0)