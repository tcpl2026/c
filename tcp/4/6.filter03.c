#include <stdio.h>
#include <ctype.h>
#include <stdlib.h>
#include <time.h>

int main()
{
    int ch, r;

    srand( (unsigned)time(NULL) );

    while ( (ch=getchar()) != EOF )
    {
        r = rand() % 2;
        if (r)
            putchar( toupper(ch) );
        else
            putchar( tolower(ch) );
    }

    return 0;
}
