import math

split_int_input = lambda: [int(v) for v in input().split()]
N, H = split_int_input()
a = [0] * N
b = [0] * N
for i in range(N):
    a[i], b[i] = split_int_input()

b = sorted(b, reverse=True)
max_a = max(a)
ans = 0
for v in b:
    if v >= max_a:
        H -= v
        ans += 1
        if H <= 0:
            print(ans)
            exit()

ans += math.ceil(H / max_a)
print(ans)