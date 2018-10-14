#include <stdio.h>
#include <math.h>

using namespace std;

struct line {
    bool order0_x, order0_y, order1;
    float x, y, a, b;
};

struct point {
    float x, y;
};

point getIntersection(struct line l1, struct line l2) {
    float X, Y;
    if (l1.order1 && l2.order1) {
        X = (l2.b-l1.b)/(l1.a-l2.b);
        Y = l1.a*X+l1.b;
    } else if (l1.order0_x) {
        X = l1.x;
        if (l2.order0_y) {
            Y = l2.y;
        } else {
            Y = l2.a*X+l2.b;
        }
    } else if (l1.order0_y) {
        Y = l1.y;
        if (l2.order0_x) {
            X = l2.x;
        } else {
            X = (Y-l2.b)/l2.a;
        }
    }
    struct point tmp;
    tmp.x = X;
    tmp.y = Y;
    return tmp;
}

float format(float input) {
    return floor(input * 1000)/1000;
}

int main() {
    int n;
    scanf("%d", &n);

    for (int i = 0; i < n; i++) {
        point A, B, C;
        scanf("%f%f%f%f%f%f", &A.x, &A.y, &B.x, &B.y, &C.x, &C.y);
        struct line l1;
        if (A.x == B.x) {
            l1.order0_y = true;
            l1.y = (A.y+B.y)/2;
        } else if (A.y == B.y) {
            l1.order0_x = true;
            l1.x = (A.x+B.x)/2;
        } else {
            l1.order1 = true;
            l1.a = -1/((A.y-B.y)/(A.x-B.x));
            l1.b = (A.y+B.y)/2 - l1.a*(A.x+B.x)/2;
        }

        struct line l2;
        if (B.x == C.x) {
            l2.order0_y = true;
            l2.y = (B.y+C.y)/2;
        } else if (B.y == C.y) {
            l2.order0_x = true;
            l2.x = (B.x+C.x)/2;
        } else {
            l2.order1 = true;
            l2.a = -1/((B.y-C.y)/(B.x-C.x));
            l2.b = (B.y+C.y)/2 - l2.a*(B.y+C.y)/2;
        }

        struct point res;
        float resR;
        res = getIntersection(l1, l2);
        resR = sqrt(pow(A.x-res.x, 2) + pow(A.y-res.y, 2));
        printf("%.3f %.3f %.3f\n", format(res.x), format(res.y), format(resR));
    }
}