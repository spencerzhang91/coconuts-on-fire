/* summing.c -- summing the user inputed integer */
#include <stdio.h>
int main(void)
{
	long num;
	long sum = 0L; // initialize sum as 0
	int status;
	
	printf("Please enter an integer to be summed. (q to quit):");
	status = scanf("%ld", &num);
	while (status == 1)
	{
		sum = sum + num;
		printf("Please enter an integer to be summed. (q to quit):");
		status = scanf("%d", &num);
	}
	printf("Those integers sum to %ld.\n", sum);
	return 0;
}
