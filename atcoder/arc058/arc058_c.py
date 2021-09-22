input_split_int = lambda: [int(v) for v in input().split()]
N, K = input_split_int()
D = set(input_split_int())


def check(n):
    while n > 0:
        d, m = divmod(n, 10)
        if m in D:
            return False
        n = d
    return True


n = N
while 1:
    if check(n):
        print(n)
        exit()
    n += 1
