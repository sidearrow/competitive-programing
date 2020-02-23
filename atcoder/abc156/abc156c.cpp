#include <bits/stdc++.h>
using namespace std;
using ll = long long;

int main() {
    int N;
    cin >> N;

    int X[N];
    int mn = -1;
    int mx = -1;
    for (int i = 0; i < N; i++) {
        cin >> X[i];
        mn = mn == -1 ? X[i] : min(mn, X[i]);
        mx = mx == -1 ? X[i] : max(mx, X[i]);
    }

    int res = -1;
    for (int i = mn; i <= mx; i++) {
        int tmp = 0;
        for (int j = 0; j < N; j++) {
            tmp += (i - X[j]) * (i - X[j]);
        }
        res = res == -1 ? tmp : min(res, tmp);
    }

    cout << res;
}
