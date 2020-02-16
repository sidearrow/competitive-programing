#include <bits/stdc++.h>
using namespace std;

int main() {
  int N, K;
  cin >> N >> K;
  vector<long long>H(N);
  for(int i = 0; i < N; i++) {
    cin >> H[i];
  }
  sort(H.begin(), H.end());

  long long res = 0;
  for (int i = 0; i < N; i++) {
    if (K > 0) {
      K--;
      continue;
    }
    res += H[i];
  }

  cout << res;
}


