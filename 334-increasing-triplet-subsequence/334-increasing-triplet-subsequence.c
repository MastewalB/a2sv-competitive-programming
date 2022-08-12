

bool increasingTriplet(int* nums, int numsSize){
    int a = INT_MAX, b = INT_MAX;
    
    for(int i = 0; i < numsSize; i++){
        int n = nums[i];
        if(n > b)
            return true;
        if(n <= a)
            a = n;
        else if(n <= b)
            b = n;
    }
    return false;
}