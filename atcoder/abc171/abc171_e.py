input_split_int = lambda: [int(v) for v in input().split()]

N = int(input())
A = input_split_int()

xor_a = 0
for a in A:
    xor_a ^= a
ans = []
for a in A:
    ans.append(xor_a ^ a)
print(*ans)