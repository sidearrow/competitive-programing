#include <stdio.h>
#include <utility>
#include <algorithm>

using namespace std;

int main() {
    while (1) {
        int n, m;
        scanf("%d%d", &n, &m);
        if (n == 0 && m == 0) {
            break;
        }
        pair<int, int> pl[m];
        bool first = true;
        while (n--) {
            for (int i = 0; i < m; i++) {
                if (first) {
                    pl[i] = make_pair(0, i+1);
                }
                int tmp;
                scanf("%d", &tmp);
                if (tmp) {
                    pl[i] = make_pair(--pl[i].first, i+1);
                }
            }
            first = false;
        }
        sort(pl, pl+m);

        for (int i = 0; i < m; i++) {
            if (i == m-1) {
                printf("%d\n", pl[i].second);
                break;
            }
            printf("%d ", pl[i].second);
        }
    }
}