#include <bits/stdc++.h>
using namespace std;

int H, W;
vector<string> S;

int bfs(int h, int w) {
    vector<vector<int>> dist(H, vector<int>(W, -1));
    queue<pair<int, int>> que;

    que.push({h, w});
    dist[h][w] = 0;
    while (!que.empty()) {
        pair<int, int> now = que.front();
        que.pop();

        for (pair<int, int> move : {make_pair(1, 0), make_pair(0, -1),
                                    make_pair(-1, 0), make_pair(0, 1)}) {
            if (now.first - move.first < 0 || now.first - move.first >= H ||
                now.second - move.second < 0 || now.second - move.second >= W) {
                continue;
            }
            if (S[now.first - move.first][now.second - move.second] == '.' &&
                dist[now.first - move.first][now.second - move.second] == -1) {
                que.push({now.first - move.first, now.second - move.second});
                dist[now.first - move.first][now.second - move.second] =
                    dist[now.first][now.second] + 1;
            }
        }
    }

    int mx = 0;
    for (vector<int> v : dist) {
        for (int i : v) {
            mx = max(i, mx);
        }
    }
    return mx;
}

int main() {
    cin >> H >> W;

    S.resize(H);
    int res = 0;
    for (int i = 0; i < H; i++) {
        cin >> S[i];
    }
    for (int i = 0; i < H; i++) {
        for (int j = 0; j < W; j++) {
            if (S[i][j] == '.') {
                res = max(res, bfs(i, j));
            }
        }
    }

    cout << res;
}
