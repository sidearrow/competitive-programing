split_int_input = lambda: [int(v) for v in input().split()]
N, M = split_int_input()
ope_lst = []
for _ in range(M):
    x, y = split_int_input()
    ope_lst.append([x - 1, y - 1])

ball_num_lst = [1] * N
red_flag_lst = [False] * N
red_flag_lst[0] = True

for x, y in ope_lst:
    ball_num_lst[x] -= 1
    ball_num_lst[y] += 1
    if red_flag_lst[x]:
        red_flag_lst[y] = True
    if ball_num_lst[x] == 0:
        red_flag_lst[x] = False

ans = sum(red_flag_lst)
print(ans)
