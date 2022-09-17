#define MAX(a, b) (((a) > (b)) ? (a) : (b))

int cmp(const void * a, const void * b){
    if((*(int **)a)[0] == (*(int **)b)[0])
        return (*(int **)a)[1] - (*(int **)b)[1];
    
    return (*(int **)a)[0] - (*(int **)b)[0];
}

int minGroups(int** intervals, int intervalsSize, int* intervalsColSize){
    qsort(intervals, intervalsSize, sizeof(int *), cmp);
    
    int N = INT_MIN, groups = 1;
    
    for(int i = 0; i < intervalsSize; i++){
        N = MAX(N, intervals[i][1]);   
    }
    
    int * intervalLine = (int *)calloc(N + 2, sizeof(int));
    
    for(int i = 0; i < intervalsSize; i++){
        intervalLine[intervals[i][0]] += 1;
        intervalLine[intervals[i][1] + 1] -= 1;
    }
    
    for(int i = 0; i < N; i++){
        if(i > 0)
            intervalLine[i] += intervalLine[i - 1];
        groups = MAX(groups, intervalLine[i]);
    }
    
    return groups;
}