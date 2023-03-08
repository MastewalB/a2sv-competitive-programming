#define MAX(a, b) (((a) > (b)) ? (a) : (b))

int minEatingSpeed(int* piles, int pilesSize, int h){
    int maxSpeed = piles[0], minSpeed = 1;
    
    for(int i = 0; i < pilesSize; i++){
        maxSpeed = MAX(maxSpeed, piles[i]);
    }
    
    while(minSpeed < maxSpeed){
        int midSpeed = (minSpeed + maxSpeed) >> 1;
        int hours = 0;
        for(int i = 0; i < pilesSize; i++){
            hours += (piles[i] > midSpeed) ? (piles[i] % midSpeed) ? (piles[i] / midSpeed) + 1: (piles[i] / midSpeed): 1;
        }
        if(hours <= h){
            maxSpeed = midSpeed;
        }else{
            minSpeed = midSpeed + 1;
        }
    }
    
    return minSpeed;
}