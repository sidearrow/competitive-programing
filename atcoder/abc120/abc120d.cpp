#include <iostream>
#include <stdio.h>
#include <vector>

using namespace std;

class UnionFind {
  public:
    vector<int> parent;

    UnionFind(int i) { parent = vector<int>(i, -1); }

    int find(int i) {
        if (parent[i] < 0) {
            return i;
        }
        return parent[i];
    }

    int size(int i) { return -parent[find(i)]; }

    void unite(int a, int b) {
        a = find(a);
        b = find(b);
        if (a == b) {
            return;
        }
        if (size(a) < size(b)) {
            swap(a, b);
        }
        parent[a] += parent[b];
        parent[b] = a;
    }
};

int main() {
    int N, M;
    scanf("%d %d", &N, &M);

    UnionFind uf = UnionFind(N);
    int a[M], b[M];
    long long ans[M];
    for (int i = 0; i < M; i++) {
        scanf("%d %d", &a[i], &b[i]);
    }

    ans[M - 1] = (long long)N * (N - 1) / 2;
    for (int i = M - 1; i > 0; i--) {
        ans[i - 1] = ans[i];
        if (uf.find(a[i] - 1) != uf.find(b[i] - 1)) {
            ans[i - 1] =
                ans[i] - (long long)uf.size(a[i] - 1) * uf.size(b[i] - 1);
            uf.unite(a[i] - 1, b[i] - 1);
        }
    }

    for (int i = 0; i < M; i++) {
        cout << ans[i] << "\n";
    }
}
