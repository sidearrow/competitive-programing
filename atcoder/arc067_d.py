split_int_input = lambda: [int(v) for v in input().split()]
N, A, B = split_int_input()
X = split_int_input()

ans = 0
now = X[0]
for x in X[1:]:
    ans += min((x - now) * A, B)
    now = x
print(ans)