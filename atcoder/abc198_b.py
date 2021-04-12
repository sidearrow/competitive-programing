N = input()
N = N.rstrip("0")
rn = "".join(list(reversed(N)))
if N == rn:
    print("Yes")
else:
    print("No")