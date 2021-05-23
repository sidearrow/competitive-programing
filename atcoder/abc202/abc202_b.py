S = input()

ans = []
for s in S:
    tmp = s
    if s == "6":
        tmp = "9"
    elif s == "9":
        tmp = "6"
    ans.append(tmp)

print("".join(reversed(ans)))