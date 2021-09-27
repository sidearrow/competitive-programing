input_split_int = lambda: [int(v) for v in input().split()]
A, B, C = input_split_int()

for i in range(A, B + 1):
    if i % C == 0:
        print(i)
        exit()
print(-1)