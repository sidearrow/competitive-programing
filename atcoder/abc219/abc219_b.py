S = [input() for _ in range(3)]
T = [int(v) - 1 for v in input()]
ans = [S[t] for t in T]
print("".join(ans))