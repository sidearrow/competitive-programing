#include <stdio.h>
#include <algorithm>

using namespace std;

int main() {
    int n;
    scanf("%d", &n);
    int _min;
    int _max = -1000000000;
    for (int i = 0; i < n; i++) {
        int tmp;
        scanf("%d", &tmp);
        if (i == 0) {
            _min = tmp;
            continue;
        }
        _max = max(_max, tmp - _min);
        _min = min(_min, tmp);
    }
    printf("%d\n", _max);
}