#include <bits/stdc++.h>
using namespace std;
using ll = long long;

bool is_prime(int n) {
    if (n < 2) return false;
    for (int i = 2; i * i <= n; i++) {
        if (n % i == 0) return false;
    }
    return true;
}

int main() {
    int X;
    cin >> X;

    bool not_found = true;
    while (not_found) {
        not_found = !is_prime(X);
        X++;
    }

    cout << X - 1;
}
