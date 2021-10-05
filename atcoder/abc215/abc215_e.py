MOD = 998244353
N = int(input())
S = [ord(c) - 65 for c in input()]


def main():
    dp = [[[0] * 10 for _ in range(1 << 10)] for _ in range(N)]
    dp[0][0][S[0]] = 1
    dp[0][1 << S[0]][S[0]] = 1
    for i in range(1, N):
        s = S[i]
        for bit in range(1 << 10):
            is_existed = bit >> s & 1 == 1
            nxt_bit = bit | (1 << s)
            for last in range(10):
                if is_existed:
                    if last == s:
                        dp[i][bit][s] += dp[i - 1][bit][last] * 2
                    else:
                        dp[i][bit][last] += dp[i - 1][bit][last]
                    dp[i][bit][s] %= MOD
                else:
                    dp[i][nxt_bit][s] += dp[i - 1][bit][last]
                    dp[i][bit][last] += dp[i - 1][bit][last]
                    dp[i][nxt_bit][s] %= MOD
                    dp[i][bit][last] %= MOD
    ans = 0
    for bit in range(1, 1 << 10):
        for last in range(10):
            ans += dp[-1][bit][last]
            ans %= MOD
    print(ans)


main()