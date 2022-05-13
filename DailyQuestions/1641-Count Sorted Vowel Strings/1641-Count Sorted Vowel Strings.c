void countVowel(char *vowels, char *buffer, int n, int *returnSize, int *bufferIndex, int startIndex);

int countVowelStrings(int n)
{
    char *vowels = "aeiou";
    char *buffer = (char *)malloc(sizeof(char) * n + 1);

    int returnSize = 0;
    int bufferIndex = 0;

    countVowel(vowels, buffer, n, &returnSize, &bufferIndex, 0);
    return returnSize;
}

void countVowel(char *vowels, char *buffer, int n, int *returnSize, int *bufferIndex, int startIndex)
{
    if (*bufferIndex == n)
    {
        (*returnSize)++;
        return;
    }

    for (int i = startIndex; i < 5; i++)
    {
        buffer[(*bufferIndex)++] = vowels[i];
        countVowel(vowels, buffer, n, returnSize, bufferIndex, i);
        (*bufferIndex)--;
    }
}