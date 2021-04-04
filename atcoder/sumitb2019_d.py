N = int(input())
S = input()

a = {""}
res = set()
for s in S:
    for t in list(a):
        t += s
        if len(t) == 3:
            res.add(t)
        else:
            a.add(t)

print(len(res))