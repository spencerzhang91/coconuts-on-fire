/* my_zippo1.c -- about zippo P267 */
#include <stdio.h>
int main(void)
{
	int zippo[10][2] = {{2,4}, {6,8}, {1,3}, {5,7}, {2,4}, {6,8}, {1,3}, {5,7}, {1,3}, {5,7}};
	
	printf("scan results below very carefully...\n");
	printf("[01]         zippo = %p\n", zippo);
	printf("[06]     zippo + 1 = %p\n", zippo + 1);
	printf("[02]        &zippo = %p\n", &zippo);
	printf("[07]    &zippo + 1 = %p\n", &zippo + 1);
	printf("[03]        *zippo = %p\n", *zippo);
	printf("[08]    *zippo + 1 = %p\n", *zippo + 1);
	printf("[04]       *&zippo = %p\n", *&zippo);
	printf("[09]   *&zippo + 1 = %p\n", *&zippo + 1);
	printf("[05]       &*zippo = %p\n", &*zippo);
	printf("[10]   &*zippo + 1 = %p\n\n", &*zippo + 1);	
	
	
	printf("[11]         zippo[0] = %p\n", zippo[0]);
	printf("[16]     zippo[0] + 1 = %p\n", zippo[0] + 1);
	printf("[12]        &zippo[0] = %p\n", &zippo[0]);
	printf("[17]    &zippo[0] + 1 = %p\n", &zippo[0] + 1);
	printf("[13]        *zippo[0] = %p\n", *zippo[0]);
	printf("[18]    *zippo[0] + 1 = %p\n", *zippo[0] + 1);
	printf("[14]       *&zippo[0] = %p\n", *&zippo[0]);
	printf("[19]   *&zippo[0] + 1 = %p\n", *&zippo[0] + 1);
	printf("[15]       &*zippo[0] = %p\n", &*zippo[0]);
	printf("[20]   &*zippo[0] + 1 = %p\n\n", &*zippo[0] + 1);	
	
	
	printf("[21]         *zippo = %p\n", *zippo);
	printf("[26]     *zippo + 1 = %p\n", *zippo + 1);
	printf("[22]        &*zippo = %p\n", &*zippo);
	printf("[27]    &*zippo + 1 = %p\n", &*zippo + 1);
	printf("[23]        **zippo = %p\n", **zippo);
	printf("[28]    **zippo + 1 = %p\n", **zippo + 1);
	printf("[24]       *&*zippo = %p\n", *&*zippo);
	printf("[29]   *&*zippo + 1 = %p\n", *&*zippo + 1);
	printf("[25]       &**zippo = %p\n", &**zippo);
	printf("[30]   &**zippo + 1 = %p\n\n", &**zippo + 1);	
	
	
	printf("[31]         zippo[0][0] = %p\n", zippo[0][0]);
	printf("[36]     zippo[0][0] + 1 = %p\n", zippo[0][0] + 1);
	printf("[31]        &zippo[0][0] = %p\n", &zippo[0][0]);
	printf("[37]    &zippo[0][0] + 1 = %p\n", &zippo[0][0] + 1);
	printf("[33]        *zippo[0][0] is invalid syntax\n");
	printf("[38]    *zippo[0][0] + 1 is invalid syntax\n");
	printf("[34]       *&zippo[0][0] = %p\n", *&zippo[0][0]);
	printf("[39]   *&zippo[0][0] + 1 = %p\n", *&zippo[0][0] + 1);
	printf("[35]       &*zippo[0][0] is invalid syntax\n");
	printf("[40]   &*zippo[0][0] + 1 is invalid syntax\n\n");
		
	
	printf("[41]         **zippo = %p\n", **zippo);
	printf("[46]     **zippo + 1 = %p\n", **zippo + 1);
	printf("[42]        &**zippo = %p\n", &**zippo);
	printf("[47]    &**zippo + 1 = %p\n", &**zippo + 1);
	printf("[43]        ***zippo is invalid syntax\n");
	printf("[48]    ***zippo + 1 is invalid syntax\n");
	printf("[44]       *&**zippo = %p\n", *&**zippo);
	printf("[49]   *&**zippo + 1 = %p\n", *&**zippo + 1);
	printf("[45]       &***zippo is invalid syntax\n");
	printf("[50]   &***zippo + 1 is invalid syntax\n\n");
	
	return 0;
}


