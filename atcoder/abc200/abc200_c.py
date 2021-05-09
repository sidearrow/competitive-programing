split_int_input = lambda: [int(v) for v in input().split()]

N = int(input())
A = split_int_input()

b = [0] * 200
for a in A:
    b[a % 200] += 1

ans = 0
for v in b:
    if v >= 2:
        ans += v * (v - 1) // 2

print(ans)
