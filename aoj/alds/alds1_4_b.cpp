#include <bits/stdc++.h>
using namespace std;
using ll = long long;

int main() {
    int n;
    cin >> n;

    int S[n];
    for (int i = 0; i < n; i++) {
        cin >> S[i];
    }

    int q;
    cin >> q;

    int t;
    int res = 0;
    for (int i = 0; i < q; i++) {
        cin >> t;
        bool is_found = binary_search(S, S + n, t);
        if (is_found) {
            res++;
        }
    }

    cout << res << "\n";
}
