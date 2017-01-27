#include <stdio.h>

/* gcc -o pointers pointers.c */
/* ./pointers */

int *add_five(int *num) {
	*num = *num + 5;
	return num;
}
 
int main()
{
	int x = 0;
    add_five(&x);
    printf("hello world %d", x);
    return 0;
}
