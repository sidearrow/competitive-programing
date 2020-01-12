#include <bits/stdc++.h>

using namespace std;

int main() {
    int N;
    cin >> N;

    double res = 0;
    double tmp;
    for (int i = 0; i < N; i++) {
        cin >> tmp;
        res += 1 / tmp;
    }

    cout << 1 / res << "\n";
}
