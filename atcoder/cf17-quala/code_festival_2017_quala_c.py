split_int_input = lambda: [int(v) for v in input().split()]

H, W = split_int_input()
A = {}
for _ in range(H):
    for s in input():
        if s not in A:
            A[s] = 0
        A[s] += 1

for h in range(H // 2):
    for w in range(W // 2):
        valid = False
        for k, v in A.items():
            if v >= 4:
                A[k] -= 4
                valid = True
                break
        if not valid:
            print("No")
            exit()

n = 0
if W % 2 == 1:
    n += H // 2
if H % 2 == 1:
    n += W // 2
for h in range(n):
    for k, v in A.items():
        valid = False
        if v >= 2:
            A[k] -= 2
            valid = True
            break
    if not valid:
        print("No")
        exit()

print("Yes")