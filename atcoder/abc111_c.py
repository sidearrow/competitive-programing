from collections import Counter

split_int_input = lambda: [int(v) for v in input().split()]
N = int(input())
V = split_int_input()

o = []
e = []
for i in range(N):
    if i % 2 == 0:
        o.append(V[i])
    else:
        e.append(V[i])

oc = Counter(o)
ec = Counter(e)

ocm = oc.most_common()
ecm = ec.most_common()
ocm.append((-1, 0))
ecm.append((-1, 0))

ans = N
if ocm[0][0] != ecm[0][0]:
    ans -= ocm[0][1]
    ans -= ecm[0][1]
else:
    tmp = max(ocm[0][1] + ecm[1][1], ocm[1][1] + ecm[0][1])
    ans -= tmp

print(ans)