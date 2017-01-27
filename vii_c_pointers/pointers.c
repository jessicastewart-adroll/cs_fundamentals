#include <stdio.h>

/* gcc -o pointers pointers.c */
/* ./pointers */

void add(int *num1, int num2) {
	*num1 = *num1 + num2;
}

void subtract(int *num1, int num2) {
	*num1 = *num1 - num2;
}

void multiply(int *num1, int num2) {
	*num1 = *num1 * num2;
}

void divide(int *num1, int num2) {
	*num1 = *num1 / num2;
}
 
int main()
{
	int x = 0;

    add(&x, 6);
    printf("Integer after addition %d\n", x);

    subtract(&x, 1);
    printf("Integer after subtraction %d\n", x);
        
    multiply(&x, 2);
    printf("Integer after multiplication %d\n", x);
        
    divide(&x, 5);
    printf("Integer after division %d\n", x);
    return 0;
}
