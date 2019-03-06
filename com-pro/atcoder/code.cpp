#include <stdio.h>

int main() {
    int n;
    scanf("%d", &n);
    int prev = 0;
    int res = 0;
    int tmp;
    for (int i = 0; i < n; i++) {
      scanf("%d", &tmp);
      if (prev < tmp) {
        res += tmp-prev;
      }
      prev = tmp;
    }
    printf("%d", res);
}