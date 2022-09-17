#define MIN(a, b) (((a) < (b)) ? (a) : (b))

int findPoisonedDuration(int* timeSeries, int timeSeriesSize, int duration){
    int total = 0;
    for(int i = 0; i < timeSeriesSize; i++){
        if(i == timeSeriesSize - 1)
            total += duration;
        else
            total += MIN(timeSeries[i + 1] - timeSeries[i], duration);
        
    }
    return total;
}