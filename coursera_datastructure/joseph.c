/* Joseph Problem */
#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>
#define MAX 300

bool kill(int *ptr, int seq, int len);
int main(void)
{
    int n, m;
    scanf("%d %d", &n, &m);
    if (n > MAX)
        n = MAX;
    if (n < 1)
        n = 1;
    if (m > MAX)
        m = MAX;
    if (m < 1)
        m = 1;
    
    int monkeys[n];
    int start = 0;
    int len = n;
    
    /* initialize array */
    for (int i = 0; i < n; i++)
        monkeys[i] = 1 + i;        
        
    while (len > 1)
    {
        kill(monkeys, (start+m-1)%len, len);
        start = (start+m-1)%len;
        len--;
    }
    printf("%d\n", monkeys[0]);
    return 0;   
}

bool kill(int *ptr, int seq, int len)
{
    if (len <= 0)
        return false;
    
    while (seq < len - 1)
    {
        ptr[seq] = ptr[seq + 1];
        seq++;
    }
    return true;    
}
