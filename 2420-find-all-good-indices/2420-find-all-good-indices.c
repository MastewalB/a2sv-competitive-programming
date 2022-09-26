

/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* goodIndices(int* nums, int numsSize, int k, int* returnSize){
    int count = 1;
    int * numsInfo = (int *)calloc(numsSize,sizeof(int));
    
    for(int i = 0; i < numsSize - k; i++){
        if(i >= k && count >= k)
            numsInfo[i] = 1;
        if(i > 0 && nums[i] > nums[i - 1])
            count = 0;
        count++;
    }
    count = 1;
    for(int i = numsSize - 1; i >= k; i--){
        if(i < numsSize - k && count >= k)
            numsInfo[i] &= 1;
        else
            numsInfo[i] = 0;
        if(i < numsSize - 1 && nums[i] > nums[i + 1])
            count = 0;
        count++;
    }
    
    int i = 0;
    *returnSize = 0;
    while(i < numsSize){
        if(numsInfo[i] == 1){
            numsInfo[(*returnSize)++] = i;
        }
        i++;
    }
    
    return numsInfo;
}