#define MAX(a, b) (((a) > (b)) ? (a) : (b))

int Comparator(const void *a , const void *b){
    return *(int *)a - *(int *)b;
}


int findPairs(int* nums, int numsSize, int k){
    int i = 0, j = 0, res = 0;
    qsort(nums, numsSize, sizeof(int), Comparator);
    
    while(i < numsSize){
        
        while( i > 0 && i < numsSize && nums[i] == nums[i - 1])
            i++;
        
        j = MAX(j, i + 1);
        while(j < numsSize && nums[j] < nums[i] + k)
            j++;
        
        if(j >= numsSize)
            return res;
        
        if(nums[j] == nums[i] + k){
            res++;
            j++;
        }
        i++;
    }
    
    return res;
}