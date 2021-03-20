#include <bits/stdc++.h>
using namespace std;

int main() {
    int N;
    cin >> N;

    int res = 0;
    int mn = 0;
    int now;
    for (int i = 0; i++; i < N) {
        cin >> now;
        if (mn >= now) {
            res++;
        }
        mn = min(mn, now);
    }
    cout << res;
}
