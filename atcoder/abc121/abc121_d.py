split_int_input = lambda: [int(v) for v in input().split()]
A, B = split_int_input()


def xor(a):
    return [a, 1, a + 1, 0][a % 4]


print(xor(A - 1) ^ xor(B))
