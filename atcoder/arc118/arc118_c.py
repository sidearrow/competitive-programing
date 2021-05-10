# n = 30000
# prime = [True] * (n + 1)
# prime[0] = prime[1] = False
# for i in range(2, int(n ** 0.5) + 1):
#    if not prime[i]:
#        continue
#    for j in range(i * 2, n + 1, i):
#        prime[j] = False
#
#
# l = []
# for i, v in enumerate(prime):
#    if v:
#        l.append(i)

N = int(input())
ans = [6, 10, 15]
cnt = 3
i = 16
while cnt < N:
    if i % 6 == 0 or i % 10 == 0 or i % 15 == 0:
        ans.append(i)
        cnt += 1
    i += 1

print(*ans)
