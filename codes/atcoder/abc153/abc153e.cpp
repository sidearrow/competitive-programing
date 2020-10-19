#include <bits/stdc++.h>
using namespace std;

int main() {
  int H, N;
  cin >> H >> N;
  vector<pair<int, int>> AB(N);
  for (int i = 0; i < N; i++) {
    cin >> AB[i].first >> AB[i].second;
  }

  long long dp[H];
  dp[0] = 0;
  for (int i = 1; i <= H; i++) {
    dp[i] = -1;
    for (int j = 0; j < N; j++) {
      int tmp = max(i - AB[j].first, 0);
      dp[i] = dp[i] == -1 ? AB[j].second + dp[tmp] : min(AB[j].second + dp[tmp], dp[i]);
    }
  }
  cout << dp[H];
}
