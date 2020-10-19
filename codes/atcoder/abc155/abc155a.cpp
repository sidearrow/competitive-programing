#include <bits/stdc++.h>
using namespace std;
using ll = long long;

int main() {
    int A, B, C;
    cin >> A >> B >> C;
    if ((A == B && B != C)
    || (A == C && A != B)
    || (B == C && B != A)) {
        cout << "Yes";
    } else {
        cout << "No";
    }
}
