input_split_int = lambda: [int(v) for v in input().split()]

N = int(input())
A = input_split_int()
Q = int(input())

ans = 0
memo = [0] * (10 ** 5 + 10)
for a in A:
    memo[a] += 1
    ans += a

for _ in range(Q):
    b, c = input_split_int()
    tmp = memo[b]
    memo[b] = 0
    memo[c] += tmp
    ans += (c - b) * tmp
    print(ans)
