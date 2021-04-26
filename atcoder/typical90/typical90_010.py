split_int_input = lambda: [int(v) for v in input().split()]

N = int(input())
CP = [split_int_input() for _ in range(N)]
Q = int(input())

st1 = [0] * (N * 2)
st2 = [0] * (N * 2)
for i, (c, p) in enumerate(CP, N):
    if c == 1:
        st1[i] = p
    else:
        st2[i] = p
for i in range(N - 1, 0, -1):
    st1[i] = st1[2 * i] + st1[2 * i + 1]
    st2[i] = st2[2 * i] + st2[2 * i + 1]


def get(st, l, r):
    l += N
    r += N
    vl, vr = 0, 0
    while l < r:
        if l % 2 == 1:
            vl += st[l]
            l += 1
        if r % 2 == 1:
            r -= 1
            vr += st[r]
        l //= 2
        r //= 2
    return vl + vr


for _ in range(Q):
    l, r = split_int_input()
    l -= 1
    ans1 = get(st1, l, r)
    ans2 = get(st2, l, r)
    print(ans1, ans2)