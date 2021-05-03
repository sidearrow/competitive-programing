s = input()
sets = set(s)
last = {v: -1 for v in sets}
maxl = {v: -1 for v in sets}
for i in range(len(s)):
    _s = s[i]
    maxl[_s] = max(maxl[_s], i - last[_s] - 1)
    last[_s] = i
for v in sets:
    maxl[v] = max(maxl[v], len(s) - last[v] - 1)
ans = min(maxl.values())
print(ans)