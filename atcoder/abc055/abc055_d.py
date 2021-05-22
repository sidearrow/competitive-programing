N = int(input())
S = input()

nxt = {
    "S": {"o": {"S": "S", "W": "W"}, "x": {"S": "W", "W": "S"}},
    "W": {"o": {"S": "W", "W": "S"}, "x": {"S": "S", "W": "W"}},
}

anss = [["S", "S"], ["S", "W"], ["W", "S"], ["W", "W"]]
for ans in anss:
    for s in S:
        a, b = ans[-1], ans[-2]
        ans.append(nxt[a][s][b])
    if ans[0] == ans[-2] and ans[1] == ans[-1]:
        print("".join(ans[1:-1]))
        exit()
print(-1)
