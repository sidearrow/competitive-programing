S = input()

ans = True
while 1:
    if len(S) == 0:
        break
    if S[-5:] == "dream":
        S = S[:-5]
        continue
    if S[-7:] == "dreamer":
        S = S[:-7]
        continue
    if S[-5:] == "erase":
        S = S[:-5]
        continue
    if S[-6:] == "eraser":
        S = S[:-6]
        continue
    ans = False
    break

print("YES" if ans else "NO")