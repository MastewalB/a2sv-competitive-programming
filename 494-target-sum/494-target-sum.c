int total(int * nums, int numsSize){
    int res = 0;
    for(int i = 0; i < numsSize; i++)
        res += nums[i];
    return res;
}


int findTargetSumWays(int* nums, int numsSize, int target){
    int sum = total(nums, numsSize);
    int totalSums = 2 * sum + 1;
    if(target < -sum || sum < target)
        return 0;
    
    int * dp = (int *)calloc(totalSums, sizeof(int));
    dp[sum] = 1;
    
    for(int i = 0; i < numsSize; i++){
        int * allSum = (int *)calloc(totalSums, sizeof(int));
        for(int j = 0; j < totalSums; j++){
            if(dp[j] != 0){
                allSum[j + nums[i]] += dp[j];
                allSum[j - nums[i]] += dp[j];
            }
        }
        dp = allSum;
    }
    
    return dp[sum + target];
}