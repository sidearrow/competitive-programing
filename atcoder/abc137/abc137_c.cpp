#include <bits/stdc++.h>

using namespace std;

int main() {
    int N;
    cin >> N;

    long long res = 0;
    unordered_map<string, int> mp;
    string tmp;
    for (int i = 0; i < N; i++) {
        cin >> tmp;
        sort(&tmp[0], &tmp[tmp.length()]);

        auto itr = mp.find(tmp);
        if (itr == mp.end()) {
            mp[tmp] = 1;
        } else {
            res += mp[tmp];
            mp[tmp]++;
        }
    }

    cout << res << "\n";
}
