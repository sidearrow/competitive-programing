#include <algorithm>
#include <iostream>
#include <stdio.h>
#include <string>
#include <vector>

int main() {
    long long n, a, b, c, d, e;
    scanf("%lld%lld%lld%lld%lld%lld", &n, &a, &b, &c, &d, &e);
    long long m = std::min({a, b, c, d, e});
    printf("%lld", (n + m - 1) / m + 4);
}
