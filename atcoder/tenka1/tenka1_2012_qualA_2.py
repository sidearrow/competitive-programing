ans = ""
prev = False
for s in input():
    if s != " ":
        ans += s
        prev = False
    else:
        if not prev:
            ans += ","
        prev = True

print(ans)