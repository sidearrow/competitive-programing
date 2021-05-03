S = input()
K = int(input())

a = []
prev = [""]
for s in S:
    new_prev = [""]
    for s2 in prev:
        s2 = s2 + s
        a_set = set(a)
        a_set.add(s2)
        a_sorted = sorted(a_set)
        if len(a_sorted) > K:
            if a_sorted[-1] == s2:
                continue
            else:
                del a_sorted[-1]
        a = a_sorted
        new_prev.append(s2)
    prev = new_prev

print(a[-1])
