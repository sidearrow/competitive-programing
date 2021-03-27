split_int_input = lambda: [int(v) for v in input().split()]
X, K, D = split_int_input()

X = abs(X)
a = K - X // D
if a < 0:
    ans = X - D * K
else:
    if a % 2 == 0:
        ans = X % D
    else:
        ans = D - X % D
print(ans)
