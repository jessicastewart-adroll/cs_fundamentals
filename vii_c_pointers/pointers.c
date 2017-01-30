#include <stdio.h>
#include <stdlib.h>

/* gcc -o pointers pointers.c */
/* ./pointers */

void add(int *num1, int *num2) {
	*num1 = *num1 + *num2;
}

void subtract(int *num1, int *num2) {
	*num1 = *num1 - *num2;
}

void multiply(int *num1, int *num2) {
	*num1 = *num1 * *num2;
}

void divide(int *num1, int *num2) {
	*num1 = *num1 / *num2;
}
 
int main(int argc, char *argv[])
{
    if (argc != 3) {
        printf("This program takes 2 arguments! Run like this: %s <integer1> <integer2>\n", argv[0]);
        return 1;
    }

	int x = atoi(argv[1]);
    int y = atoi(argv[2]);

    printf("Integers %d %d\n", x, y);

    add(&x, &y);
    printf("Integer after addition %d %d\n", x, y);

    subtract(&x, &y);
    printf("Integer after subtraction %d %d\n", x, y);
        
    multiply(&x, &y);
    printf("Integer after multiplication %d %d\n", x, y);
        
    divide(&x, &y);
    printf("Integer after division %d %d\n", x, y);

    return 0;
}
