#include <stdio.h>

int main() {
    int a[4];
    scanf("%d%d%d%d", &a[0], &a[1], &a[2], &a[3]);
    bool b = false;
    bool c = false;
    bool d = false;
    bool e = false;
    for (int i = 0; i < 4; i++) {
        if (!b && a[i] == 1) {
            b = true;
        } else if (a[i] == 9) {
            c = true;
        } else if (a[i] == 7) {
            d = true;
        } else if (a[i] == 4) {
            e = true;
        }
    }
    if (b && c && d && e) {
        printf("YES");
    } else {
        printf("NO");
    }
}
