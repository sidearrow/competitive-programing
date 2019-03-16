#include <stdio.h>

int main() {
  int tmp = 9;
  for (int i = 10; i < 20; i++) {
    tmp = tmp xor i;
    printf("%d\n", tmp);
  }
}
