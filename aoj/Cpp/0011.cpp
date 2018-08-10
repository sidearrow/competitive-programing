#include <stdio.h>
#include <utility>

using namespace std; 

int main() {
    int w, n;
    scanf("%d%d", &w, &n);
    int num[w];
    for (int i = 0; i < w; i++) {
        num[i] = i+1;
    }
    while (n--) {
        int i, j;
        scanf("%d,%d", &i, &j);
        swap(num[i-1], num[j-1]);
    }
    for (int i = 0; i < w; i++) {
        printf("%d\n", num[i]);
    }
}