#include <stdio.h>
#include <iostream>
#include <vector>
#include <algorithm>
#include <string>

int main() {
    int L[10] = {0, 2, 5, 5, 4, 5, 6, 3, 7, 6};
    int N, M;
    scanf("%d%d", &N, &M);
    int A[M];
    for (int i = 0; i < M; i++) {
        scanf("%d", &A[i]);
    }
    std::sort(A, A+M, std::greater<>());

    std::vector<int> dp(N, -1);
    for (int i = 1; i < N; i++) {
        for (int j = 0; j < M; j++) {
            if (i - L[A[j]] > 0) {
                dp[i] = std::max(dp[i], dp[i-L[A[j]]] + 1);
            }
        }
    }

    int cur = 1;
    std::string res = "";
    int i = 0;
    while (cur < N) {
        for (int i = 0; i < M; i++) {
            if (dp[cur] == dp[cur+L[A[i]]]-1) {
                res.push_back(A[i] + '0');
                cur += L[A[i]];
                break;
            }
        }
        i++;
        if (i == 100) {
            break;
        }
    }
    std::cout << res << "\n";
}
