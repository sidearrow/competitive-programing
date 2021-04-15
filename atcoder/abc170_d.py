split_int_input = lambda: [int(v) for v in input().split()]
N = int(input())
A = split_int_input()

maxa = max(A)
multis = [False] * (maxa + 1)
counts = [0] * (maxa + 1)

for a in A:
    counts[a] += 1
    if counts[a] > 1:
        continue
    tmp = a
    while 1:
        tmp += a
        if tmp > maxa:
            break
        multis[tmp] = True

ans = 0
for a in A:
    if counts[a] == 1 and not multis[a]:
        ans += 1

print(ans)