split_int_input = lambda: [int(v) for v in input().split()]

N, K = split_int_input()
l = [0] * (10 ** 5 + 10)
for _ in range(N):
    a, b = split_int_input()
    l[a] += b

tmp = 0
ans = -1
for i in range(1, 10 ** 5 + 11):
    tmp += l[i]
    if tmp >= K:
        ans = i
        break

print(ans)
