#include <iostream>
#include <stdio.h>
#include <string>

using namespace std;

int main() {
    string a = "keyence";
    string b;
    cin >> b;
    int bl = (int)b.size();
    bool res = true;
    for (int i = 0; i < bl; i++) {
        if (a[i] != b[i]) {
            if (b.substr(bl - 7 + i, 7 - i) != a.substr(i, 7 - i)) {
                res = false;
            }
            break;
        }
    }
    if (res) {
        printf("YES");
    } else {
        printf("NO");
    }
}
