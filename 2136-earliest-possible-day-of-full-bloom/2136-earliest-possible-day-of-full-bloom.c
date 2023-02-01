#define MAX(a, b) (((a) > (b)) ? (a) : (b))

int compare(const void *a, const void *b){
    return (*(int **)b)[1] - (*(int **)a)[1];
}

int earliestFullBloom(int* plantTime, int plantTimeSize, int* growTime, int growTimeSize){
    int ** bloom = (int **)malloc(plantTimeSize * sizeof(int *));
    int days = 0, nextPlant = 0;
    
    for(int i = 0; i < plantTimeSize; i++){
        bloom[i] = (int *)malloc(sizeof(int) * 2);
        bloom[i][0] = plantTime[i];
        bloom[i][1] = growTime[i];
    }
    
    qsort(bloom, plantTimeSize, sizeof(int *), compare);
    
    for(int i = 0; i < plantTimeSize; i++){
        int duration = nextPlant + bloom[i][0] + bloom[i][1];
        days = MAX(days, duration);
        nextPlant = nextPlant + bloom[i][0];
    }
    return days;
}