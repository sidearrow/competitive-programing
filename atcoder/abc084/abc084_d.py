split_int_input = lambda: [int(v) for v in input().split()]
Q = int(input())
LR = [split_int_input() for _ in range(Q)]


def is_prime(n):
    for i in range(3, int(n ** 0.5) + 1, 2):
        if n % i == 0:
            return False
    return True


is_prime_list = [False] * (10 ** 5 + 10)
is_prime_list[2] = True
cnt = 0
cnt_list = [0, 0, 0]
for i in range(3, 10 ** 5 + 1):
    if i % 2 == 1 and is_prime(i):
        is_prime_list[i] = True
        if is_prime_list[(i + 1) // 2]:
            cnt += 1
    cnt_list.append(cnt)

for l, r in LR:
    print(cnt_list[r] - cnt_list[l - 1])
