#include <stdio.h>
#include <iostream>
#include <string>

using namespace std;

int main() {
    string S;
    cin >> S;
    int l = S.length();
    int x, y;
    x = y = 0;
    for (int i = 0; i < l; i++) {
        if (i % 2 == 0) {
            if (S[i] == '0') {
                y++;
            } else {
                x++;
            }
        } else {
            if (S[i] == '0') {
                x++;
            } else {
                y++;
            }
        }
    }
    printf("%d", min(x, y));
}
