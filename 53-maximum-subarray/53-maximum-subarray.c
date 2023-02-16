#define MAX(a, b) (((a) > (b)) ? (a) : (b))

int maxSubArray(int* nums, int numsSize){
    int max = INT_MIN, running = 0;
    
    for(int i = 0; i < numsSize; i++){
        running += nums[i];
        max = MAX(running, max); //The subarray with minimum sum
        if(running < 0) // the subarray with the minimum subarray removed
            running = 0;
    }
    return max;
    
}