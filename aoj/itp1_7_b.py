def solve(n: int, x: int):
    res = 0
    for i in range(1, n + 1):
        for j in range(i + 1, n + 1):
            k = x - i - j
            if k > j and k <= n:
                res += 1
    return res


def main():
    while 1:
        n, x = map(int, input().split())
        if n == 0 and x == 0:
            break
        result = solve(n, x)
        print(result)


if __name__ == "__main__":
    main()
