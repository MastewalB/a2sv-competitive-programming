

int change(int amount, int* coins, int coinsSize){
    int * ways = (int *)calloc(amount + 1, sizeof(int));
    ways[0] = 1;
    
    for(int j = 0; j < coinsSize; j++){
        for(int i = 1; i <= amount; i++){
            if(coins[j] <= i)
                ways[i] += ways[i - coins[j]];
        }
    }
    
    return ways[amount];
}