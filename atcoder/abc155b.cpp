#include <bits/stdc++.h>
using namespace std;
using ll = long long;

int main() {
    int N;
    cin >> N;
    bool res = true;
    int tmp;
    for (int i = 0; i < N; i++) {
        cin >> tmp;
        if (tmp % 2 != 0 || tmp % 3 == 0 || tmp % 5 == 0) {
            continue;
        }
        res = false;
    }
    if (res) {
        cout << "APPROVED";
    } else {
        cout << "DENIED";
    }
}
