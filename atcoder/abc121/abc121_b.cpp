#include <stdio.h>

int main() {
    int N, M, C;
    scanf("%d%d%d", &N, &M, &C);
    int B[M];
    for (int i=0; i<M; i++) {
      scanf("%d", &B[i]);
    }
    int res = 0;
    int temp;
    int A;
    for (int i=0; i<N; i++) {
      temp = C;
      for (int j=0; j<M; j++) {
        scanf("%d", &A);
        temp += A*B[j];
      }
      if (temp > 0) {
        res++;
      }
    }
    printf("%d", res);
}
