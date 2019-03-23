#include <stdio.h>
#include <algorithm>

using namespace std;

struct process {
    char name[10];
    int time;
};

const int len = 100005;
int head, tail;
process Q[len];

void enqueue(process p) {
    Q[tail] = p;
    tail = (tail + 1) % len;
}

process dequeue() {
    process p = Q[head];
    head = (head + 1) % len;
    return p;
}

int main() {
    int n, q;
    int now = 0;
    scanf("%d %d", &n, &q);
    for (int i = 0; i < n; i++) {
        char name[10];
        int time;
        scanf("%s %d", Q[i].name, &Q[i].time);
    }
    head = 0;
    tail = n;

    process tmp;
    int consum;
    int remain;
    while (head != tail) {
        tmp = dequeue();
        consum = min(tmp.time, q);
        now += consum;
        tmp.time -= consum;
        if (tmp.time != 0) {
            enqueue(tmp);
            continue;
        }
        printf("%s %d\n", tmp.name, now);
    }
}
