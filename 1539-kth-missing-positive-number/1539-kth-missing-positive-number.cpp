class Solution {
public:
    int findKthPositive(vector<int>& arr, int k) {
        int low = 0, high = arr.size();
        
        while(low < high){
            int mid = (low + high) / 2;
            int diff = arr[mid] - (mid + 1);
            if(diff < k)
                low = mid + 1;
            else
                high = mid;
        }
        return low + k;
    }
};