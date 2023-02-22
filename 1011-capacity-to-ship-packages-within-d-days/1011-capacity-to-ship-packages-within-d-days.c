#define MAX(a, b) (((a) > (b)) ? (a) : (b))

int shipWithinDays(int* weights, int weightsSize, int days){
    int minWeight = weights[0], totalWeight = 0;
    
    for(int i = 0; i < weightsSize; i++){
        totalWeight += weights[i];
        minWeight = MAX(minWeight, weights[i]);
    }
    
    while(minWeight < totalWeight){
        int midWeight = (minWeight + totalWeight) >> 1;
        int dayCount = 1, curr = 0;
        
        for(int i = 0; i < weightsSize; i++){
            if(curr + weights[i] > midWeight){
                dayCount++;
                curr = 0;
            }
            curr += weights[i];
        }
        if(dayCount > days)
            minWeight = midWeight + 1;
        else
            totalWeight = midWeight;
    }
    
    return minWeight;
}