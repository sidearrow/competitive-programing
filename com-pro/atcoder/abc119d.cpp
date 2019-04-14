#include <stdio.h>
#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

const long long inf = 200000000001;

int main() {
    int A, B, Q;
    scanf("%d%d%d", &A, &B, &Q);

    vector<long long> s(A+2), t(B+2);
    s[0] = -inf;
    t[0] = -inf;
    s[A+1] = inf;
    t[B+1] = inf;
    for (int i = 1; i <= A; i++) {
        scanf("%lld", &s[i]);
    }
    for (int i = 1; i <= B; i++) {
        scanf("%lld", &t[i]);
    }

    long long q, res;
    for (int i = 0; i < Q; i++) {
        scanf("%lld", &q);
        int si = lower_bound(s.begin(), s.end(), q) - s.begin();
        int ti = lower_bound(t.begin(), t.end(), q) - t.begin();
        res = min({
            abs(q-s[si]) + abs(s[si]-t[ti]),
            abs(q-s[si]) + abs(s[si]-t[ti-1]),
            abs(q-s[si-1]) + abs(s[si-1]-t[ti]),
            abs(q-s[si-1]) + abs(s[si-1]-t[ti-1]),
            abs(q-t[ti]) + abs(t[ti]-s[si]),
            abs(q-t[ti]) + abs(t[ti]-s[si-1]),
            abs(q-t[ti-1]) + abs(t[ti-1]-s[si]),
            abs(q-t[ti-1]) + abs(t[ti-1]-s[si-1])
        });
        printf("%lld\n", res);
    }
}
