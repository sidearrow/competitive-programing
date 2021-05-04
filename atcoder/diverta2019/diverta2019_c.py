N = int(input())
S = [input() for _ in range(N)]

a = 0
b = 0
ab = 0
ans = 0
for s in S:
    isa = s[-1] == "A"
    isb = s[0] == "B"
    if isb and isa:
        ab += 1
    elif isb:
        b += 1
    elif isa:
        a += 1
    for i in range(len(s) - 1):
        if s[i] == "A" and s[i + 1] == "B":
            ans += 1
if ab > 0:
    ans += ab - 1
    if a > 0:
        a -= 1
        ans += 1
    if b > 0:
        b -= 1
        ans += 1
ans += min(a, b)
print(ans)