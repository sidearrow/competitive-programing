N = int(input())
S = input()

l = 0
ans = ""
for s in S:
    if s == "(":
        l += 1
        ans += "("
        continue
    if l > 0:
        ans += ")"
        l -= 1
    else:
        ans = "(" + ans + ")"
ans += ")" * l
print(ans)