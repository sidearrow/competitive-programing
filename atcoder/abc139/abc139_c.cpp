#include <bits/stdc++.h>

using namespace std;

int main() {
    int N;
    cin >> N;

    int res = 0;
    int move = 0;
    int prev;
    int now;
    for (int i = 0; i < N; i++) {
        if (i == 0) {
            cin >> prev;
            continue;
        }
        cin >> now;
        if (now > prev) {
            res = max(res, move);
            move = 0;
        } else {
            move++;
        }
        prev = now;
    }
    res = max(res, move);

    cout << res;
}
