#include <stdio.h>
#include <stdlib.h>

int S[200];
int top = 0;

void push(int i) {
    S[++top] = i;
}

int pop() {
    top--;
    return S[top+1];
}

int main() {
    char c[10];
    while (scanf("%s", c) != EOF) {
        if (c[0] == '+') {
            int x = pop();
            int y = pop();
            push(x+y);
            continue;
        }
        if (c[0] == '-') {
            int x = pop();
            int y = pop();
            push(y-x);
            continue;
        }
        if (c[0] == '*') {
            int x = pop();
            int y = pop();
            push(x*y);
            continue;
        }
        push(atoi(c));
    }

    printf("%d\n", pop());
}
