#include <iostream>

using namespace std;

int main () {
    while (true) {
        int x;
        cin >> x;
        if (cin.eof()) {
            break;
        }
        if (x > 36) {
            cout << 0 << endl;
            continue;
        }
        int i = 0;
        for (int a = 0; a < 10 && x - a >= 0; a++) {
            int _a = x - a;
            if (_a > 27) {
                continue;
            }
            for (int b = 0; b < 10 && _a - b >= 0; b++) {
                int _b = _a - b;
                if (_b > 18) {
                    continue;
                }
                for (int c = 0; c < 10 && _b - c >= 0; c++) {
                    int _c = _b - c;
                    if (_c > 9) {
                        continue;
                    }
                    i++;
                }
            }
        }
        cout << i << endl;
    }
}