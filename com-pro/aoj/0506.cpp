#include <stdio.h>
#include <iostream>
#include <string>

using namespace std;

int main() {
    while (1) {
        int n;
        scanf("%d", &n);
        if (n == 0) {
            break;
        }

        string now, tmp;
        cin >> now;
        int size;
        int cnt = 0;
        char before = ' ';
        for (int i = 0; i< n; i++) {
            tmp = now;
            size = tmp.size();
            for (int j = 0; j < size; j++) {
                if (j == 0) {
                    now = "";
                    cnt = 1;
                } else {
                    if (before == tmp[j]) {
                        cnt++;
                    } else {
                        now += to_string(cnt) + before;
                        cnt = 1;
                    }
                }
                
                before = tmp[j];
                if (j == size-1) {
                    now += to_string(cnt) + before;
                }
            }
        }
        cout << now << "\n";
    }
}