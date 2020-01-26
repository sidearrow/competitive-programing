#include <bits/stdc++.h>
using namespace std;

int main() {
    int N;
    cin >> N;

    int count[10][10];
    for (int i = 0; i < 10; i++) {
        for (int j = 0; j < 10; j++) {
            count[i][j] = 0;
        }
    }

    for (int i = 1; i <= N; i++) {
        string str = to_string(i);
        int head = stoi(str.substr(0, 1));
        int tail = stoi(str.substr(str.length() - 1, 1));

        count[head][tail]++;
    }

    int res = 0;
    for (int i = 1; i < 10; i++) {
        for (int j = 1; j < 10; j++) {
            res += count[i][j] * count[j][i];
        }
    }

    cout << res;
}
