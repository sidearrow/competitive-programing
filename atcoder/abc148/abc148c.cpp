#include <bits/stdc++.h>
using namespace std;
using ll = long long;

ll gcd(ll a, ll b) {
    return b == 0 ? a : gcd(b, a % b);
}

int main() {
    ll A, B;
    cin >> A >> B;

    cout << A * B / gcd(A, B);
}
