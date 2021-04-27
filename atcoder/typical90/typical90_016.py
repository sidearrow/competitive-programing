split_int_input = lambda: [int(v) for v in input().split()]

N = int(input())
A, B, C = sorted(split_int_input(), reverse=True)


ans = 10000
for i1 in range(N // A + 1):
    sum_a = A * i1
    for i2 in range((N - sum_a) // B + 1):
        sum_c = N - sum_a - B * i2
        if sum_c % C == 0:
            i3 = sum_c // C
            ans = min(ans, i1 + i2 + i3)

print(ans)