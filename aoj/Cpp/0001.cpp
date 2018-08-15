#include <stdio.h>
#include <algorithm>
#include <functional>
 
using namespace std;
 
int main() {
    int input[10];
    for (int i = 0; i < 10; i++) {
        scanf("%d", &input[i]);
    }
    sort(input, input+10, greater<int>());
    for (int i = 0; i < 3; i++) {
        printf("%d\n", input[i]);
    }
}