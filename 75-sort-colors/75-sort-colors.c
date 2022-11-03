void swap(int * nums, int i, int j){
    int temp = nums[i];
    nums[i] = nums[j];
    nums[j] = temp;
}

void sortColors(int* nums, int numsSize){
    int smaller = 0, greater = numsSize - 1, white = 1;
    
    int i = 0;
    while(i <= greater && i < numsSize){
        if(nums[i] < white){
            swap(nums, i, smaller);
            i++;
            smaller++;
        }else if(nums[i] > white){
            swap(nums, i, greater);
            greater--;
        }else{
            i++;
        }
        
    }
}