split_int_input = lambda: [int(v) for v in input().split()]

N, M = split_int_input()
PY = []

for i in range(M):
    p, y = split_int_input()
    PY.append([p, y, i])

PY = sorted(PY, key=lambda v: v[1])

pdict = {}
PY2 = []
for p, y, i in PY:
    if p not in pdict:
        pdict[p] = 1
    else:
        pdict[p] += 1
    PY2.append([p, pdict[p], i])

PY2 = sorted(PY2, key=lambda v: v[2])

for i in range(M):
    p, i, _ = PY2[i]
    print(str(p).zfill(6) + str(i).zfill(6))
