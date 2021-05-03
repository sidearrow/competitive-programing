split_int_input = lambda: [int(v) for v in input().split()]
N = int(input())
A = split_int_input()

ans = float("INF")
for bit in range(1 << (N - 1)):
    tmp = 0
    _or = 0
    for i in range(N - 1):
        _or |= A[i]
        if bit >> i & 1:
            tmp ^= _or
            _or = 0
    _or |= A[-1]
    tmp ^= _or
    ans = min(ans, tmp)

print(ans)