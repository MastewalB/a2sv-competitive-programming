#include <stdio.h>
/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
void combine(char **result, char **phone, char *digits, char *temp, int index, int *resLen);
char **letterCombinations(char *digits, int *returnSize)
{
    char *phone[8] = {"abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"};
    char **result = (char **)malloc(sizeof(char *) * 4000);

    char temp[strlen(digits) + 1];
    int resLen = 0;
    if (strlen(digits) == 0)
    {
        *returnSize = resLen;
        return result;
    }
    combine(result, phone, digits, temp, 0, &resLen);
    *returnSize = resLen;
    return result;
}

void combine(char **result, char **phone, char *digits, char *temp, int index, int *resLen)
{
    if (index == strlen(digits))
    {
        temp[index] = 0;
        result[(*resLen)] = (char *)malloc(strlen(temp) + 1);
        strcpy(result[(*resLen)], temp);
        (*resLen)++;
        return;
    }

    char *phoneData = phone[digits[index] - '0' - 2];
    for (int i = 0; i < strlen(phoneData); i++)
    {
        temp[index] = phoneData[i];
        combine(result, phone, digits, temp, index + 1, resLen);
    }
}