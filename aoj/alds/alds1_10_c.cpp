#include <bits/stdc++.h>

using namespace std;

int slv(string x, string y) {
    int lx = x.length();
    int ly = y.length();
    int dp[lx + 1][ly + 1];
    for (int i = 0; i <= lx; i++) {
        dp[i][0] = 0;
    }
    for (int i = 0; i <= ly; i++) {
        dp[0][i] = 0;
    }
    for (int ix = 1; ix <= lx; ix++) {
        for (int iy = 1; iy <= ly; iy++) {
            if (x[ix - 1] != y[iy - 1]) {
                dp[ix][iy] = max(dp[ix][iy - 1], dp[ix - 1][iy]);
                continue;
            }
            dp[ix][iy] = dp[ix - 1][iy - 1] + 1;
        }
    }

    return dp[lx][ly];
}

int main() {
    int n;
    scanf("%d", &n);

    string x, y;
    for (int i = 0; i < n; i++) {
        cin >> x >> y;
        cout << slv(x, y) << "\n";
    }
}
