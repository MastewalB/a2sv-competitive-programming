int jump(int* nums, int numsSize){
    int position = numsSize - 1;
    int steps = 0;
    
    while( position != 0){
        for ( int i = 0; i < position; i++ ){
            if (nums[i] + i >= position){
                position = i;
                steps++;
                break;
            }
        }
    }
    return steps;
}