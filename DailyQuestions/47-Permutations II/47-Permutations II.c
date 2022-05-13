#include <stdlib.h>
#include <stdbool.h>
/**
 * Return an array of arrays of size *returnSize.
 * The sizes of the arrays are returned as *returnColumnSizes array.
 * Note: Both returned array and *columnSizes array must be malloced, assume caller calls free().
 */
void permute(int **result, int *nums, int numsSize, int startIndex, int *resultIndex);
void swap(int *nums, int src, int dest);

int **permuteUnique(int *nums, int numsSize, int *returnSize, int **returnColumnSizes)
{
    int **result = (int **)malloc(50000 * sizeof(int *));
    // int * buffer = (int *)malloc(numsSize * sizeof(int));
    int resultIndex = 0;
    int startIndex = 0;
    permute(result, nums, numsSize, startIndex, &resultIndex);
    *returnColumnSizes = (int *)malloc(resultIndex * sizeof(int));
    for (int i = 0; i < resultIndex; i++)
    {
        (*returnColumnSizes)[i] = numsSize;
    }
    *returnSize = resultIndex;
    return result;
}

void permute(int **result, int *nums, int numsSize, int startIndex, int *resultIndex)
{
    if (startIndex == numsSize)
    {
        result[*resultIndex] = (int *)malloc(numsSize * sizeof(int));
        memcpy(result[(*resultIndex)], nums, numsSize * sizeof(int));
        (*resultIndex)++;
        return;
    }

    bool set[21] = {0};
    for (int i = startIndex; i < numsSize; i++)
    {
        if (set[nums[i] + 10])
            continue;
        set[nums[i] + 10] = true;
        swap(nums, startIndex, i);
        permute(result, nums, numsSize, startIndex + 1, resultIndex);
        swap(nums, startIndex, i);
    }
}

void swap(int *nums, int src, int dest)
{
    int temp = nums[src];
    nums[src] = nums[dest];
    nums[dest] = temp;
}