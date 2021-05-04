split_int_input = lambda: [int(v) for v in input().split()]
N = int(input())
A = split_int_input()
B = split_int_input()

p_sum = 0
m_sum = 0
for i in range(N):
    tmp = A[i] - B[i]
    if tmp < 0:
        m_sum += -tmp // 2
    else:
        p_sum += tmp

if m_sum >= p_sum:
    print("Yes")
else:
    print("No")