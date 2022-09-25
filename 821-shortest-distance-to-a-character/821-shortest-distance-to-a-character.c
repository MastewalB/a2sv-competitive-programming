#define MIN(a, b) (((a) < (b)) ? (a) : (b))

/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* shortestToChar(char * s, char c, int* returnSize){
    int N = strlen(s);
    int * res = (int *)malloc(sizeof(int) * N);
    
    int prev = N + 1;
    
    for(int i = 0; i < N; i++){
        if(s[i] == c){
            prev = i;
            res[i] = 0;
        }
        else
            res[i] = (prev < N) ? i - prev : INT_MAX;
    }
    
    prev = N + 1;
    for(int i = N - 1;  i >= 0; i--){
        if(s[i] == c)
            prev = i;
        else
            res[i] = (prev < N) ? MIN(res[i], prev - i) : res[i];
            
    }
    
    *returnSize = N;
    return res;
}