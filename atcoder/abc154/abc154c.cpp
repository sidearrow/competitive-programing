#include <bits/stdc++.h>
using namespace std;
using ll = long long;

int main() {
    int N;
    cin >> N;

    ll A[N];
    for (int i = 0; i < N; i++) {
        cin >> A[i];
    }

    bool res = false;
    unordered_map<int, bool> mp;
    for (int i = 0; i < N; i++) {
        if (mp[A[i]] == true) {
            res = true;
            break;
        }
        mp[A[i]] = true;
    }

    if (res) {
        cout << "NO";
    } else {
        cout << "YES";
    }
}
