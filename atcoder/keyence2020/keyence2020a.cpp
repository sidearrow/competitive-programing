#include <bits/stdc++.h>

using namespace std;

int main() {
    int H, W, N;
    cin >> H >> W >> N;

    int mx = max(H, W);

    cout << (N + mx - 1) / mx;
}
