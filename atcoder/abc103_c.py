split_int_input = lambda: [int(v) for v in input().split()]
N = int(input())
A = split_int_input()

ans = sum(A) - N
print(ans)