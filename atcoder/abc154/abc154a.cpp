#include <bits/stdc++.h>
using namespace std;
using ll = long long;

int main() {
    string S, T, U;
    int A, B;
    cin >> S >> T >> A >> B >> U;

    if (U == S) {
        A--;
    } else {
        B--;
    }

    cout << A << ' ' << B;
}
