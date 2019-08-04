#include <bits/stdc++.h>

using namespace std;

int vv(int m) {
    if (m < 100) {
        return 0;
    }
    if (m <= 5000) {
        return m * 10 / 1000;
    }
    if (m <= 30000) {
        return m / 1000 + 50;
    }
    if (m <= 70000) {
        return (m / 1000 - 30) / 5 + 80;
    }
    return 89;
}

int main() {
    int m;
    cin >> m;

    cout << setw(2) << setfill('0') << vv(m) << "\n";
}
