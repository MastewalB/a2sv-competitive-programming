int countSubarray(int * nums, int numsSize, int bound){
    int total = 0, j = 0;
    for(int i = 0; i < numsSize; i++){
        if(nums[i] < bound)
            total += ++j;
        else
            j = 0;
    }
    return total;
                        
}

int numSubarrayBoundedMax(int* nums, int numsSize, int left, int right){
    return countSubarray(nums, numsSize, right + 1) - countSubarray(nums, numsSize, left);
}