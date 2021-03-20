def solve(l: list, search_num: int):
    n = len(l)
    res = [False] * (search_num + 1)
    for bit in range(1 << n):
        tmp = 0
        for i in range(n):
            if bit & (1 << i):
                tmp += l[i]
        if tmp <= search_num:
            res[tmp] = True
    return res


def main():
    n = int(input())
    a = [int(v) for v in input().split()]
    q = int(input())
    m = [int(v) for v in input().split()]
    max_m = max(m)
    res = solve(a, max_m)
    for v in m:
        print("yes" if res[v] else "no")


main()