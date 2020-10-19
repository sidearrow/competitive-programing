#include <bits/stdc++.h>
using namespace std;

int solve(int n, int x) {
    int res = 0;
    for (int i = 1; i <= n; i++) {
        for (int j = i + 1; j <= n; j++) {
            for (int k = j + 1; k <= n; k++) {
                if (i + j + k == x) {
                    res++;
                }
            }
        }
    }

    return res;
}

int main() {
    int n, x;
    while (true) {
        cin >> n >> x;
        if (n == 0 && x == 0) {
            break;
        }
        cout << solve(n, x) << "\n";
    }
}
