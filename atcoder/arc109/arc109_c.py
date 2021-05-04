split_int_input = lambda: [int(v) for v in input().split()]

N, K = split_int_input()
S = list(input())


def jkn(a, b):
    s = set([a, b])
    if s == set(["R", "P"]):
        return "P"
    if s == set(["P", "S"]):
        return "S"
    if s == set(["S", "R"]):
        return "R"
    return a


for _ in range(K):
    tmp_s = []
    if len(S) % 2 == 1:
        S += S
    for i in range(len(S) // 2):
        tmp_s.append(jkn(S[i * 2], S[i * 2 + 1]))
    S = tmp_s

print(S[0])