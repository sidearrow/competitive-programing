#include <bits/stdc++.h>

using namespace std;

int main() {
    int a;
    int b;
    int c;
    int n;
    int res = 0;

    scanf("%d", &n);
    for (int i = 0; i < n; i++) {
        a = b;
        b = c;
        scanf("%d", &c);

        if (i <= 1) {
            continue;
        }

        if (
            (a < b && b < c)
            || (a > b && b > c)
        ) {
            res++;
        }
    }

    printf("%d", res);
}
