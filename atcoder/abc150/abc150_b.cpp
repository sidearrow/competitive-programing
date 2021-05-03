#include <bits/stdc++.h>
using namespace std;

int main() {
    int N;
    cin >> N;

    int res = 0;
    char p2, p1, now;
    for (int i = 0; i < N; i++) {
        cin >> now;

        if (p2 == 'A' && p1 == 'B' && now == 'C') {
            res++;
        }

        p2 = p1;
        p1 = now;
    }

    cout << res;
}
