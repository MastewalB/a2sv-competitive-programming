#include <stdio.h>
/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int *sortArrayByParity(int *nums, int numsSize, int *returnSize)
{
    int *a = (int *)malloc(numsSize * sizeof(int));
    for (int i = 0, even = 0, odd = numsSize - 1; i < numsSize; i++)
    {
        (nums[i] % 2 == 0) ? (a[even++] = nums[i]) : (a[odd--] = nums[i]);
    }
    *returnSize = numsSize;
    return a;
}