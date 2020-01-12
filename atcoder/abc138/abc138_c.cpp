#include <bits/stdc++.h>

using namespace std;

int main() {
    int N;
    cin >> N;

    int v[N];
    int tmp;
    for (int i = 0; i < N; i++) {
        cin >> v[i];
    }

    sort(&v[0], &v[N]);
    double res = v[0];
    for (int i = 1; i < N; i++) {
        res = (res + v[i]) / 2;
    }

    cout << res << "\n";
}
