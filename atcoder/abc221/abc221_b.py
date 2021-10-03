S = list(input())
T = list(input())


def check(a, b):
    for _a, _b in zip(a, b):
        if _a != _b:
            return False
    return True


if check(S, T):
    print("Yes")
    exit()

for i in range(len(S) - 1):
    S[i], S[i + 1] = S[i + 1], S[i]
    if check(S, T):
        print("Yes")
        exit()
    S[i], S[i + 1] = S[i + 1], S[i]

print("No")
