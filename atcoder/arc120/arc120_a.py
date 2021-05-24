split_int_input = lambda: [int(v) for v in input().split()]

N = int(input())
A = split_int_input()

maxa = []
suma = []
sumb = []
tmpm = 0
tmpsa = 0
tmpsb = 0
for a in A:
    tmpm = max(tmpm, a)
    tmpsa += a
    maxa.append(tmpm)
    suma.append(tmpsa)
    sumb.append(tmpsb)
    tmpsb += suma[-1]

for i in range(N):
    ans = maxa[i] * (i + 1) + suma[i] + sumb[i]
    print(ans)
