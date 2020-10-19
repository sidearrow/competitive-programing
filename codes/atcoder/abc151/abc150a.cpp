#include <bits/stdc++.h>

using namespace std;

int main() {
    string str = "abcdefghijklmnopqrstuvwxyz";
    string c;
    cin >> c;
    int i = str.find(c);
    cout << str[i + 1];
}
