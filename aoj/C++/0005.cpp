#include<cstdio>
#include<iostream>

using namespace std;

int main () {
    long long a, b, c, d, e;
    while (scanf("%d %d", &a, &b) != EOF) {
        c = (a >= b) ? a : b;
        d = (a < b) ? a : b;
        while (d != 0) {
            e = c % d;
            c = d;
            d = e;
        }
        cout <<c<<" "<<a * b / c<< endl;
    }
}