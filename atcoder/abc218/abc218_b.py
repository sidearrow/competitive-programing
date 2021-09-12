split_int_input = lambda: [int(v) for v in input().split()]

P = split_int_input()
ans = []
for i in P:
    ans.append(chr(96 + i))
print("".join(ans))