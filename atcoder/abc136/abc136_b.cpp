#include <bits/stdc++.h>

using namespace std;
int main() {
    int N;
    cin >> N;
    if (N < 10) {
        cout << N;
        return 0;
    }
    if (N < 100) {
        cout << 9;
        return 0;
    }
    if (N <= 999) {
        cout << N - 90;
        return 0;
    }
    if (N < 10000) {
        cout << 909;
        return 0;
    }
    if (N <= 99999) {
        cout << N - 9090;
        return 0;
    }
    cout << 90909;
}
