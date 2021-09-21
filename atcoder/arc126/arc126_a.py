T = int(input())


def solve(n2, n3, n4):
    if n3 // 2 >= (n2 // 2 + n4):
        return n2 // 2 + n4
    ans = n3 // 2
    if n3 // 2 >= n4:
        n2 -= (n3 // 2 - n4) * 2
        ans += n2 // 5
        return ans
    n4 -= n3 // 2
    if n4 // 2 >= n2:
        return ans + n2
    ans += n4 // 2
    n2 -= n4 // 2
    if n4 % 2 == 1 and n2 >= 3:
        n2 -= 3
        ans += 1
    return ans + n2 // 5


for _ in range(T):
    n2, n3, n4 = [int(v) for v in input().split()]
    ans = solve(n2, n3, n4)
    print(ans)