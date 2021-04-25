split_int_input = lambda: [int(v) for v in input().split()]

N = int(input())
S = split_int_input()
Q = int(input())
T = split_int_input()

st = set()
for s in S:
    st.add(s)

ans = 0
for t in T:
    if t in st:
        ans += 1

print(ans)