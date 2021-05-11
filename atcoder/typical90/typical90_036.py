split_int_input = lambda: [int(v) for v in input().split()]

N, Q = split_int_input()
a = []
b = []
for _ in range(N):
    x, y = split_int_input()
    a.append(x + y)
    b.append(x - y)
max_a, min_a = max(a), min(a)
max_b, min_b = max(b), min(b)

for _ in range(Q):
    i = int(input())
    _a, _b = a[i - 1], b[i - 1]
    ans = max(
        abs(max_a - _a),
        abs(min_a - _a),
        abs(max_b - _b),
        abs(min_b - _b),
    )
    print(ans)
