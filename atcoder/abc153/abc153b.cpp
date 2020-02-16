#include <bits/stdc++.h>
using namespace std;

int main() {
  int H, N;
  cin >> H >> N;
  int sum = 0;
  for (int i = 0; i < N; i++) {
    int input;
    cin >> input;
    sum += input;
  }
  if (H > sum) {
    cout << 'No';
  } else {
    cout << 'Yes';
  }
}
