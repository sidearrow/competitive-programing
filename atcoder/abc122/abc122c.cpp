#include <iostream>
#include <stdio.h>
#include <string>

using namespace std;

int main() {
    int N, Q;
    scanf("%d%d", &N, &Q);

    string S;
    cin >> S;

    int a[N];
    a[0] = 0;
    for (int i = 1; i < N; i++) {
        if (S[i - 1] == 'A' && S[i] == 'C') {
            a[i] = a[i - 1] + 1;
        } else {
            a[i] = a[i - 1];
        }
    }
    int l, r;
    for (int i = 0; i < Q; i++) {
        scanf("%d%d", &l, &r);
        printf("%d\n", a[r - 1] - a[l - 1]);
    }
}
