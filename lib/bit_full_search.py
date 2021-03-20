# http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=ALDS1_5_A&lang=ja

N = 5

for bit in range(1 << N):
    l = []
    for i in range(N):
        if bit & (1 << i):
            l.append(i)
    print(l)