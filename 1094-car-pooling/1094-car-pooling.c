int cmp(const void * a, const void * b){
    if((*(int **)a)[1] == (*(int **)b)[1])
        return (*(int **)a)[2] - (*(int **)b)[2];
    return (*(int **)a)[1] - (*(int **)b)[1];
}

bool carPooling(int** trips, int tripsSize, int* tripsColSize, int capacity){
    
    qsort(trips, tripsSize, sizeof(int *), cmp);
    
    int * trip = (int *)calloc(1001, sizeof(int));
    
    for(int i = 0; i < tripsSize; i++){
        trip[trips[i][1]] += trips[i][0];
        trip[trips[i][2]] -= trips[i][0];
    }
    
    for(int i = 0; i < 1001; i++){
        if(i > 0)
            trip[i] += trip[i - 1];
        if(trip[i] > capacity)
            return false;
    }
    return true;
    
}