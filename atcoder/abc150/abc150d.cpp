#include <bits/stdc++.h>
using namespace std;
using ll = long long;

ll gcd(ll a, ll b) { return b == 0 ? a : gcd(b, a % b); }
ll lcm(ll a, ll b) { return a * b / gcd(a, b); }

int main() {
    ll N, M;
    cin >> N >> M;

    int now, lcm;
    for (int i = 0; i < N; i++) {
        cin >> now;
        if (i == 0) {
            lcm = now;
        } else {
            lcm = now * lcm / gcd(lcm, now);
        }
    }

    long long cnt = M / (lcm / 2);

    cout << (cnt + 2 - 1) / 2;
}
