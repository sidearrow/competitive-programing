import collections

S = input()

new_s = collections.deque()
is_reverse = False
for s in S:
    if s == "R":
        is_reverse = not is_reverse
    else:
        if is_reverse:
            new_s.appendleft(s)
        else:
            new_s.append(s)

if is_reverse:
    new_s = reversed(new_s)

ans = collections.deque()
for s in new_s:
    if len(ans) > 0 and ans[-1] == s:
        ans.pop()
    else:
        ans.append(s)

print("".join(ans))
