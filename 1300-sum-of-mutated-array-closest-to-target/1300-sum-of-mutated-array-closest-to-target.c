#define MAX(a, b) (((a) > (b)) ? (a) : (b))
#define MIN(a, b) (((a) < (b)) ? (a) : (b))

int findBestValue(int* arr, int arrSize, int target){
    int max = INT_MIN, total = 0;
    
    for(int i = 0; i < arrSize; i++){
        max = MAX(max, arr[i]);
        total += arr[i];
    }
        
    
    if(total <= target)
        return max;
    
    
    int left = 0, right = max, ans = INT_MAX, diff = INT_MAX;
    while(left <= right){
        int mid = (left + right) >> 1;
        int localSum = 0;
        for(int i = 0; i < arrSize; i++)
            localSum += (arr[i] > mid) ? mid : arr[i];
        
        if(abs(localSum - target) < diff){
            ans = mid;
            diff = abs(localSum - target);
        }else if(abs(localSum - target) == diff)
            ans = MIN(ans, mid);
        if(localSum > target){
            right = mid - 1;
        }
        else{
            left = mid + 1;
        }
    }
    return ans;
}