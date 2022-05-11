#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>

bool isIsomorphic(char *s, char *t)
{
    int charSet[129];
    int mapSet[129];
    for (int i = 0; i < 129; i++)
    {
        charSet[i] = -1;
        mapSet[i] = -1;
    }

    while (*s)
    {
        if (charSet[*s] >= 0)
        {
            if (charSet[*s] != *t)
            {
                return false;
            }
        }
        else if (mapSet[*t] >= 0)
        {
            return false;
        }
        else
        {
            charSet[*s] = *t;
            mapSet[*t] = *s;
        }
        s++;
        t++;
    }
    return true;
}