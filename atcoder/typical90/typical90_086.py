input_split_int = lambda: [int(v) for v in input().split()]

MOD = 1000000007
N, Q = input_split_int()
XYZW = [input_split_int() for _ in range(Q)]

ans = 1
for i in range(60):
    cnt = 0
    for j in range(1 << N):
        isok = True
        for x, y, z, w in XYZW:
            _w = ((j >> (x - 1)) | (j >> (y - 1)) | (j >> (z - 1))) & 1
            if _w != (w >> i & 1):
                isok = False
                break
        if isok:
            cnt += 1
    ans = (ans * cnt) % MOD

print(ans)
