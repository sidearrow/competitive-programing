#include <bits/stdc++.h>
using namespace std;

int main() {
    int N;
    cin >> N;

    int res = 0;
    int mn = 0;
    int now;
    for (int i = 0; i < N; i++) {
        cin >> now;
        if (i == 0 || mn >= now) {
            res++;
            mn = now;
        }
    }
    cout << res;
}
