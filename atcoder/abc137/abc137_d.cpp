#include <bits/stdc++.h>

using namespace std;

int main() {
    int N, M;
    cin >> N >> M;

    pair<int, int> p[N];
    for (int i = 0; i < N; i++) {
        cin >> p[i].first >> p[i].second;
    }

    sort(p, p + N, [](pair<int, int> x, pair<int, int> y) {
        return x.first < y.first;
    });

    priority_queue<int> pq;
    long long res = 0;
    int j = 0;
    for (int i = 1; i <= M; i++) {
        while (j < N && p[j].first <= i) {
            pq.push(p[j].second);
            j++;
        }
        if (!pq.empty()) {
            res += pq.top();
            pq.pop();
        }
    }

    cout << res << "\n";
}
