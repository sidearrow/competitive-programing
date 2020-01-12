#include <bits/stdc++.h>

using namespace std;

int main() {
    int N;
    cin >> N;

    int res = 0;
    int now;
    int prev;
    for (int i = 0; i < N - 1; i++) {
        cin >> now;
        if (i == 0) {
            res += now;
        } else {
            res += min(prev, now);
        }
        prev = now;
    }
    res += now;

    cout << res;
}
