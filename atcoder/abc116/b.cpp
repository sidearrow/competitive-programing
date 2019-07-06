#include <stdio.h>

int main() {
    int s;
    scanf("%d", &s);
    int a = 0;
    if (s == 4 || s == 2 || s == 1) {
      printf("%d", 4);
    } else {
      for (int i = 0; i < 1000000; i++) {
        if (s % 2 == 0) {
          s = s/2;
        } else {
          s = 3*s+1;
        }
        if (s == 4) {
          a++;
        }
        if (a == 2) {
          printf("%d", i+2);
          break;
        }
      }
    }
}