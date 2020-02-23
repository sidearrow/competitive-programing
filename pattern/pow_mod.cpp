#include<bits/stdc++.h>
using namespace std;
using ll = long long;

ll pow_mod(ll a, ll n, ll mod) {
    if (n == 1) {
        return a % mod;
    }
    if (n % 2 == 0) {
        ll tmp = pow_mod(a, n / 2, mod);
        return tmp * tmp % mod;
    }
    return a * pow_mod(a, n - 1, mod) % mod;
}

int main() {
    cout << pow_mod(2, 4, 6);
}
