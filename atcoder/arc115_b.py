split_int_input = lambda: [int(v) for v in input().split()]


N = int(input())
C = [split_int_input() for _ in range(N)]

a = []
b = []
for row in C:
    m = min(row)
    b.append([col - m for col in row])
    a.append(m)

for i in range(1, N):
    for j in range(N):
        if b[0][j] != b[i][j]:
            print("No")
            exit()

print("Yes")
print(*a)
print(*b[0])