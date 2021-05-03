#include <bits/stdc++.h>

using namespace std;

int main() {
    int N;
    cin >> N;

    int A[N], B[N];
    for (int i = 0; i <= N; i++) {
        cin >> A[i];
    }

    int bfr = 0;
    long long res = 0;
    int tmp = 0;
    int target = 0;

    for (int i = 0; i < N; i++) {
        cin >> tmp;
        target = min(A[i], tmp + bfr);
        res += target;
        bfr = min(tmp + bfr - target, tmp);
    }

    cout << res + min(bfr, A[N]);
}
