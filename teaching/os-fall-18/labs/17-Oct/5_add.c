#include<stdio.h>

int main(){

	int x = 100;
	asm("incl %0": "+r"(x)
	);
	printf("Value of x is %d",x);

}
