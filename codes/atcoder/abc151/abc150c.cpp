#include <bits/stdc++.h>

using namespace std;

int main() {
    int N, M;
    cin >> N >> M;
    int res[N];
    for (int i = 0; i < N; i++) {
        res[i] = 0;
    }
    int numAc = 0;
    int numWa = 0;
    int nowI;
    string nowRes;
    for (int i = 0; i < M; i++) {
        cin >> nowI >> nowRes;
        if (res[nowI - 1] == -1) {
            continue;
        }
        if (nowRes == "WA") {
            res[nowI - 1]++;
        } else {
            numAc++;
            numWa += res[nowI - 1];
            res[nowI - 1] = -1;
        }
    }
    cout << numAc << " " << numWa;
}
