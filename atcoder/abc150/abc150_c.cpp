#include <bits/stdc++.h>
using namespace std;

int main() {
    int N;
    cin >> N;

    int a[N], b[N];
    for (int i = 0; i < N; i++) {
        cin >> a[i];
    }
    for (int i = 0; i < N; i++) {
        cin >> b[i];
    }

    int seq[N];
    for (int i = 1; i <= N; i++) {
        seq[i - 1] = i;
    }

    int resa, resb;
    int cnt = 1;
    do {
        for (int i = 0; i < N; i++) {
            if (a[i] == seq[i]) {
                if (i == N - 1) {
                    resa = cnt;
                }
            } else {
                break;
            }
        }
        for (int i = 0; i < N; i++) {
            if (b[i] == seq[i]) {
                if (i == N - 1) {
                    resb = cnt;
                }
            } else {
                break;
            }
        }
        cnt++;
    } while (next_permutation(seq, seq + N));

    cout << abs(resa - resb);
}
