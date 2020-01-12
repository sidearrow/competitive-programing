#include <bits/stdc++.h>

using namespace std;

int main() {
    char c[4];

    for (int i = 0; i < 4; i++) {
        scanf("%s", &c[i]);
    }

    if ((c[0] == c[1] && c[2] == c[3] && c[1] != c[2]) ||
        (c[0] == c[2] && c[1] == c[3] && c[1] != c[2]) ||
        (c[0] == c[3] && c[1] == c[2] && c[0] != c[1])) {
        printf("%s", "Yes");
    } else {
        printf("%s", "No");
    }
}
