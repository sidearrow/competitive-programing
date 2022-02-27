import sys

readline = sys.stdin.readline
readline2 = lambda: [int(v) for v in readline().split()]

N, K = readline2()
A = readline2()

mod_to_idx = {}
mod_to_sum = {}

a = 0
mod_a = 0
memo = []
loop_end_idx = None
for i in range(K):
    a += A[mod_a]
    mod_a = a % N
    memo.append(a)
    if mod_a in mod_to_idx:
        loop_end_idx = i
        break
    mod_to_idx[mod_a] = i
    mod_to_sum[mod_a] = a

if loop_end_idx is None:
    print(memo[-1])
    exit()

loop_start_idx = mod_to_idx[mod_a]
diffidx = loop_end_idx - loop_start_idx
diff = a - mod_to_sum[mod_a]

d, m = divmod(K - loop_start_idx - 1, diffidx)

ans = diff * d + memo[loop_start_idx + m]

print(ans)