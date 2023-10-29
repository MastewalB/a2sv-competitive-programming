#include <stdio.h>
#include <string.h>

int main(void)
{
    char first[100];
    char second[100];

    scanf("%s", first);
    scanf("%s", second);

    printf("%d\n", strcmp(strlwr(first), strlwr(second)));
    return 0;
}

char *strlwr(char *s)
{
}