#include <stdio.h>
#include <vector>
#include <algorithm>
#include <map>

using namespace std;

int main() {
    int N, M;
    scanf("%d%d", &N, &M);
    vector<pair<long, long>> A(N);
    for (int i=0; i<N; i++) {
      A[i] = make_pair(0, 0);
      scanf("%ld%ld", &A[i].first, &A[i].second);
    }
    sort(A.begin(), A.end());

    long res = 0;
    int tmp;
    for (int i=0; i<N; i++) {
      tmp = M-A[i].second;
      if (tmp < 0) {
        res += M*A[i].first;
        break;
      }
      M = tmp;
      res += A[i].first*A[i].second;
    }

    printf("%ld", res);
}
