#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>
#include <assert.h>
#include <string.h>

char *build(char *s);
char *build2(char *s);
bool backspaceCompare(char *s, char *t)
{
    char *st = build(s);
    char *tt = build(t);
    return strcmp(st, tt) == 0;
}

char *build2(char *s)
{

    int lenStr = strlen(s);
    int j = 0;
    for (int i = 0; i < lenStr; i++)
    {
        if (s[i] != '#')
        {
            s[j] = s[i];
            j++;
        }
        else
        {
            if (j > 0)
                j--;
        }
    }
    s[j] = '\0';

    return s;
}

//
char *build(char *s)
{
    char *a;
    int size = 1;
    int count = 0;
    char hashtag = '#';

    a = (char *)malloc(size * sizeof(char));
    assert(a);

    while (*s)
    {

        if (*s != hashtag)
        {
            while (count >= size)
            {
                size *= 2;
                a = realloc(a, sizeof(char) * size);
            }
            a[count++] = *s;
        }
        else if (count > 0)
            count--;

        s++;
    }
    size += 1;
    a = realloc(a, sizeof(char) * size);
    a[count++] = '\0';
    a = realloc(a, sizeof(char) * count);

    return a;
}