#include <stdio.h>
#include <iostream>
#include <vector>
#include <algorithm>
#include <string>

int main() {
    long long n, a, b, c, d, e;
    scanf("%lld%lld%lld%lld%lld%lld", &n, &a, &b, &c, &d, &e);
    long long m = std::min({a, b, c, d, e});
    printf("%lld", (n+m-1)/m+4);
}
