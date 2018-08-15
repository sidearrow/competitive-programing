#include <stdio.h>

int main() {
    int a, b, result, sum;
    while (scanf("%d %d", &a, &b) != EOF) {
        result = 0;
        sum = a+b;
        while (sum != 0) {
            sum /= 10;
            printf("%d\n", sum);
            result++;
        }
        printf("%d\n", result);
    }
}