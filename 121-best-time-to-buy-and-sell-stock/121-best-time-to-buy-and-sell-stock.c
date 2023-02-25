#define MAX(a, b) (((a) > (b)) ? (a) : (b))

int maxProfit(int* prices, int pricesSize){
    int profit = 0, bestBuy = INT_MIN;   // bestBuy keeps the best day we spend minimum if we buy
    
    bestBuy = profit - prices[0]; //if we buy on the first day we'll have a negative profit
    
    for(int i = 1; i < pricesSize; i++){
        // on the subsquent days we'll have three choices 
        // 1 - to determine if it's the best day to buy rather than the previous best day i.e. 0 - prices[i]
        // 2 - to check if the profit is better if we sell i.e. bestBuy + prices[i] ----> bestbuy is cost and prices[i] is gain
        // 3 - to do nothing 
        
        profit = MAX(profit, prices[i] + bestBuy); // choice 2 if profit gets bigger else choice 3 
        bestBuy = MAX(bestBuy, -prices[i]); // choice 1
    }
    return profit;
}