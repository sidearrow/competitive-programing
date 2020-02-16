#include <bits/stdc++.h>
using namespace std;

int main() {
  long long H;
  cin >> H;

  int cnt = 0;
  while (H > 0) {
    cnt++;
    if (H == 1) {
      H = 0;
      continue;
    }
    H /= 2;
  }

  long long res = 0;
  long long num = 1;
  for (int i = 0; i < cnt; i++) {
    res += num;
    num *= 2;
  }

  cout << res;
}
