
#define MAX(a, b) (((a) > (b)) ? (a) : (b))
int longestOnes(int* nums, int numsSize, int k){
    int i = 0;
    int zero_count = 0;
    int total = 0;
    for(int j = 0; j < numsSize; j++){
        if(nums[j] == 0){
            zero_count++;
        }
        while(zero_count > k){
            if(nums[i] == 0){
                zero_count--;
            }
            i++;
        }
        total = MAX(total, (j - i + 1));
    }
    return total;
}