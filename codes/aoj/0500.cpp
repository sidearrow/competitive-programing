#include <stdio.h>

int main() {
    while (1) {
        int n;
        scanf("%d", &n);
        if (n == 0) {
            break;
        }

        int a, b;
        a = 0;
        b = 0;
        while (n--) {
            int _a, _b;
            scanf("%d%d", &_a, &_b);
            if (_a > _b) {
                a += _a + _b;
            } else if (_a < _b) {
                b += _b + _a;
            } else {
                a += _a;
                b += _b;
            }
        }
        printf("%d %d\n", a, b);
    }
}