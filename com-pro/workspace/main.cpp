#include <stdio.h>
#include <iostream>
#include <string>
#include <vector>
#include <utility>

using namespace std;

int main() {
    int N, K;
    scanf("%d%d", &N, &K);
    string S;
    cin >> S;
    vector<pair<int, int>> v;
    char tmp = '1';
    for (int i = 0; i < N; i++) {
        if (tmp == '1' && S[i] == '0') {
            pair<int, int> p;
            p.first = i - 1;
            p.second = -1;
            v.push_back(p);
        }
        if (tmp == '0' && S[i] == '1') {
            v[v.size()-1].second = i-1;
        }
        tmp = S[i];
    }
    for (pair<int, int> p : v) {
        printf("%d,%d\n", p.first, p.second);
    }
    int vs = v.size();
    int res = 0;
    for (int i = 0; i < vs-K+1; i++) {
        printf("%d,%d\n", v[i+K].first, v[i-1].second);
        if (i == 0) {
            res = max(res, v[i+K].first-0);
        } else if (i == vs-K) {
            res = max(res, N-v[i-1].second-1);
        } else {
            res = max(res, v[i+K].first-v[i-1].second-1);
        }
    }
    printf("%d", res);
}
