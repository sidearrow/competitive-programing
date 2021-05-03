import sys

input = sys.stdin.readline


def str_to_list(s: str):
    tmp = [0] * 10
    for i in range(4):
        tmp[int(s[i])] += 1
    return tmp


def list_to_score(l: list):
    res = 0
    for i in range(1, 10):
        res += i * (10 ** l[i])
    return res


K = int(input())
S = str_to_list(input())
T = str_to_list(input())

card = [K - S[i] - T[i] for i in range(10)]

s = 0
t = 0
for i in range(1, 10):
    tmp_card = [*card]
    if tmp_card[i] <= 0:
        continue
    tmp_card[i] -= 1
    new_s = [*S]
    new_s[i] += 1
    s_score = list_to_score(new_s)
    for j in range(1, 10):
        if tmp_card[j] <= 0:
            continue
        new_t = [*T]
        new_t[j] += 1
        t_score = list_to_score(new_t)
        if s_score > t_score:
            s += card[i] * tmp_card[j]
        else:
            t += card[i] * tmp_card[j]

print(s / (s + t))
