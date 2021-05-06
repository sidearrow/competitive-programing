N = int(input())
S1 = input()
S2 = input()

i = 0
ans = 1
MOD = 10 ** 9 + 7
prev_tate = False
while i < N:
    tmp = 1
    if S1[i] != S2[i]:
        if i == 0:
            tmp = 6
        else:
            tmp = 3 if prev_tate else 2
        i += 2
        prev_tate = True
    else:
        if i == 0:
            tmp = 3
        else:
            tmp = 1 if prev_tate else 2
        i += 1
        prev_tate = False
    ans = ans * tmp % MOD

print(ans)