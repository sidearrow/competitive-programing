#include <bits/stdc++.h>
using namespace std;
using ll = long long;

int main() {
    int N, K;
    cin >> N >> K;

    int res = 0;
    int tmp = 1;
    while (true) {
        if (N < tmp) {
            break;
        }
        tmp *= K;
        res++;
    }

    cout << res;
}
