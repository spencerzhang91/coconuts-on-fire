/* use: fopen(), fprintf(), putc(), fclose() */
#include <stdio.h>
#include <stdlib.h>

int main(void)
{
    FILE *fp;    
    char file[20];

    puts("Enter filename: \n");
    gets(file);
    fp = fopen(file, "w");
    fprintf(fp, "What the fuck is that?");
    fprintf(fp, "\nI don't know.\n");
    for (int i = 0; i < 10; i++)
        putc('c', fp);

    if (fclose(fp) != 0)
        printf("Fail to close file %s.\n", file);
    return 0;
}
