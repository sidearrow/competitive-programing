S = input()

memo = [0, 0, 0]
mapping = {"a": 0, "b": 1, "c": 2}
for s in S:
    memo[mapping[s]] += 1

if memo.count(0) == 2:
    if len(S) == 1:
        print("YES")
    else:
        print("NO")
elif memo.count(0) == 1:
    if len(S) == 2:
        print("YES")
    else:
        print("NO")
else:
    if max(memo) - min(memo) <= 1:
        print("YES")
    else:
        print("NO")