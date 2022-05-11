#include <stdio.h>
#include <stdlib.h>

void help(int **result, int *res_count, int *buf, int *i_buf, int *nums, int index, int k, int n)
{
    if (*i_buf == k && n == 0)
    {
        result[*res_count] = malloc(k * sizeof(int));
        memcpy(result[*res_count], buf, k * sizeof(int));
        (*res_count)++;
        return;
    }

    for (int i = index; i < 9; i++)
    {
        buf[(*i_buf)++] = nums[i];
        help(result, res_count, buf, i_buf, nums, i + 1, k, n - nums[i]);
        (*i_buf)--;
    }
}

/**
 * Return an array of arrays of size *returnSize.
 * The sizes of the arrays are returned as *returnColumnSizes array.
 * Note: Both returned array and *columnSizes array must be malloced, assume caller calls free().
 */
int **combinationSum3(int k, int n, int *returnSize, int **returnColumnSizes)
{
    *returnSize = 0;

    int *nums = malloc(9 * sizeof(int));
    for (int i = 1; i <= 9; i++)
        nums[i - 1] = i;

    int **result = malloc(sizeof(int *) * 16);

    int *buf = malloc(10 * sizeof(int));
    int i_buf = 0;

    help(result, returnSize, buf, &i_buf, nums, 0, k, n);

    *returnColumnSizes = malloc((*returnSize) * sizeof(int));
    for (int i = 0; i < *returnSize; i++)
    {
        (*returnColumnSizes)[i] = k;
    }

    return result;
}