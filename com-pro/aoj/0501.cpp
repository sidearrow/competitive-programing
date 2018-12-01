#include <stdio.h>

int main() {
    while (1) {
        int n;
        scanf("%d", &n);
        if (n == 0) {
            break;
        }

        char conv[n][2];
        for (int i = 0; i < n; i++) {
            scanf(" %c %c", &conv[i][0], &conv[i][1]);
        }
        int m;
        scanf("%d", &m);
        while (m--) {
            char c;
            scanf(" %c", &c);
            for (int i = 0; i < n; i++) {
                if (c == conv[i][0]) {
                    printf("%c", conv[i][1]);
                    break;
                }
                if (i == n-1) {
                    printf("%c", c);
                }
            }
        }
        printf("\n");
    }
}