#include <stdio.h>
#include <iostream>
#include <string>
#include <map>

using namespace std;

int main() {
    string S, T;
    cin >> S;
    cin >> T;

    int l = S.length();

    map<char, pair<int, int> > m;
    m.insert(make_pair('a', make_pair(-1, -1)));
    m.insert(make_pair('b', make_pair(-1, -1)));
    m.insert(make_pair('c', make_pair(-1, -1)));
    m.insert(make_pair('d', make_pair(-1, -1)));
    m.insert(make_pair('e', make_pair(-1, -1)));
    m.insert(make_pair('f', make_pair(-1, -1)));
    m.insert(make_pair('g', make_pair(-1, -1)));
    m.insert(make_pair('h', make_pair(-1, -1)));
    m.insert(make_pair('i', make_pair(-1, -1)));
    m.insert(make_pair('j', make_pair(-1, -1)));
    m.insert(make_pair('k', make_pair(-1, -1)));
    m.insert(make_pair('l', make_pair(-1, -1)));
    m.insert(make_pair('m', make_pair(-1, -1)));
    m.insert(make_pair('n', make_pair(-1, -1)));
    m.insert(make_pair('o', make_pair(-1, -1)));
    m.insert(make_pair('p', make_pair(-1, -1)));
    m.insert(make_pair('q', make_pair(-1, -1)));
    m.insert(make_pair('r', make_pair(-1, -1)));
    m.insert(make_pair('s', make_pair(-1, -1)));
    m.insert(make_pair('t', make_pair(-1, -1)));
    m.insert(make_pair('u', make_pair(-1, -1)));
    m.insert(make_pair('v', make_pair(-1, -1)));
    m.insert(make_pair('w', make_pair(-1, -1)));
    m.insert(make_pair('x', make_pair(-1, -1)));
    m.insert(make_pair('y', make_pair(-1, -1)));
    m.insert(make_pair('z', make_pair(-1, -1)));

    bool ans = true;
    for (int i = 0; i < l; i++) {
        if (m[S[i]].first != m[T[i]].second) {
            ans = false;
            break;
        }
        m[S[i]].first = i;
        m[T[i]].second = i;
    }

    if (ans) {
        printf("Yes");
    } else {
        printf("No");
    }

    return 0;
}