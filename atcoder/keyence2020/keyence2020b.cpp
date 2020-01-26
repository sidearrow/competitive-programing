#include <bits/stdc++.h>

using namespace std;

int main() {
    int N;
    cin >> N;
    vector<pair<int , int>>XL(N);
    for (int i = 0; i < N; i++) {
        cin >> XL[i].first >> XL[i].second;
    }
    sort(XL.begin(), XL.end());

    int res1 = 1;
    int last1 = XL[0].first + XL[0].second;
    for (int i = 1; i < N; i++) {
        if (XL[i].first - XL[i].second < last1) {
            continue;
        }
        res1++;
        last1 = XL[i].first + XL[i].second;
    }
    int res2 = 1;
    int last2 = XL[N - 1].first - XL[N - 1].second;
    for (int i = N - 2; i >= 0; i--) {
        if (XL[i].first + XL[i].second > last2) {
            continue;
        }
        res2++;
        last2 = XL[i].first - XL[i].second;
    }

    cout << max(res1, res2);
}
