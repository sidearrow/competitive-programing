#include <bits/stdc++.h>

using namespace std;

int main() {
    int N, K, M;
    cin >> N >> K >> M;
    int sum = 0;
    int tmp;
    for (int i = 0; i < N - 1; i++) {
        cin >> tmp;
        sum += tmp;
    }
    int res = M * N - sum;
    if (res > K) {
        cout << -1;
    } else {
        if (res < 0) {
            cout << 0;
        } else {
            cout << res;
        }
    }
}
