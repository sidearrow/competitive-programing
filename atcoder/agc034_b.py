s = input()
s = s.replace("BC", "D")

ans = 0
tmp = 0
for c in s:
    if c == "A":
        tmp += 1
    elif c == "D":
        ans += tmp
    else:
        tmp = 0

print(ans)