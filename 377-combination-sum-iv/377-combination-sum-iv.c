int cmp(const void * a, const void * b){
    return *(int *)a - *(int *)b;
}

int combinationSum4(int* nums, int numsSize, int target){
    unsigned int * comb = (unsigned int *)calloc(target + 1, sizeof(unsigned int));
    comb[0] = 1;
    
    qsort(nums, numsSize, sizeof(int), cmp);
    for(int i = 1; i <= target; i++){
        for(int j = 0; j < numsSize; j++){
            if(nums[j] <= i)
                comb[i] += comb[i - nums[j]];
            else
                break;
        }
    }
    return comb[target];
}