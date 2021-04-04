S = input()
T = input()

idx = -1
for i in range(len(S) - len(T), -1, -1):
    _a = True
    for j in range(len(T)):
        if S[i + j] == "?":
            continue
        if S[i + j] != T[j]:
            _a = False
            break
    if _a:
        idx = i
        break

if idx == -1:
    print("UNRESTORABLE")
else:
    ans = S
    ans = S[:idx] + T + S[idx + len(T) :]
    ans = ans.replace("?", "a")
    print(ans)
