#include <bits/stdc++.h>

using namespace std;
int main() {
    int N;
    cin >> N;
    int mx = 0;
    int now;
    bool res = true;
    for (int i = 0; i < N; i++) {
        cin >> now;
        if (mx - now > 1) {
            res = false;
            break;
        }
        mx = max(now, mx);
    }
    if (res) {
        cout << "Yes"
             << "\n";
    } else {
        cout << "No"
             << "\n";
    }
}
