#include <bits/stdc++.h>
using namespace std;
using ll = long long;

int main() {
    int N;
    cin >> N;
    unordered_map<string, int> S;
    string str;
    int mx = 0;
    for (int i = 0; i < N; i++) {
        cin >> str;
        if (S.find(str) == S.end()) {
            S[str] = 0;
        } else {
            S[str]++;
            mx = max(mx, S[str]);
        }
    }
    vector<string> res;
    for (auto v : S) {
        if (v.second == mx) {
            res.push_back(v.first);
        }
    }
    sort(res.begin(), res.end());

    for (auto v : res) {
        cout << v << "\n";
    }
}
