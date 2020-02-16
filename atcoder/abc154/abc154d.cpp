#include <bits/stdc++.h>
using namespace std;
using ll = long long;

int main() {
    int N, K;
    cin >> N >> K;

    double p[N];
    for (int i = 0; i < N; i++) {
        cin >> p[i];
        p[i] = (p[i] + 1) / 2;
    }

    double mx = 0;
    double now = 0;
    for (int i = 0; i < N; i++) {
        if (i < K) {
            now += p[i];
            mx = now;
            continue;
        }
        now = now + p[i] - p[i - K];
        mx = max(mx, now);
    }

     printf("%.12f", mx);
}
