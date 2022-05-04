#include <stdio.h>

int compare_ints(void *key1, void *key2)
{
    return *((int *)key1) - *((int *)key2);
}

int maxOperations(int *nums, int numsSize, int k)
{
    qsort(nums, numsSize, sizeof(int), compare_ints);

    int left = 0, right = numsSize - 1, op = 0;

    while (left < right && nums[left] < k)
    {
        int val = nums[left] + nums[right];
        if (val > k)
            right--;
        else if (val < k)
            left++;
        else
        {
            left++, right--, op++;
        }
    }
    return op;
}