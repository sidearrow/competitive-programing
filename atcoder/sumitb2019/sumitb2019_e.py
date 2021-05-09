split_int_input = lambda: [int(v) for v in input().split()]

N = int(input())
A = split_int_input()

ans = 1
memo = [0, 0, 0]
mod = 10 ** 9 + 7
for a in A:
    tmp = 0
    for i in range(3):
        if a == memo[i]:
            tmp += 1
            if tmp == 1:
                memo[i] += 1
    ans = ans * tmp % mod

print(ans)
