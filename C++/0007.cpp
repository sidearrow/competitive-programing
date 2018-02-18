#include<iostream>
#include<math.h>

using namespace std;

int main () {
    int a;
    cin >> a;
    int b = 100000;
    while (a--) {
        b = ceil(b * 1.05 / 1000) * 1000;
    }
    cout << b << endl;
}