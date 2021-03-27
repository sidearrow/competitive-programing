split_int_input = lambda: [int(v) for v in input().split()]
N = int(input())
a = split_int_input()

cnt = [0] * (10 ** 5 + 10)
for i in range(N):
    cnt[a[i] - 1] += 1
    cnt[a[i] + 1] += 1
    cnt[a[i]] += 1
ans = max(cnt)

print(ans)