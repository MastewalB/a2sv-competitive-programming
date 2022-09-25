#define MIN(a, b) (((a) < (b)) ? (a) : (b))

/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* shortestToChar(char * s, char c, int* returnSize){
    int N = strlen(s);
    int * res = (int *)malloc(sizeof(int) * N);
    int prev = INT_MAX;
    
    for(int i = 0; i < N; i++){
        if(s[i] == c)
            prev = i;
        res[i] = abs(prev - i);
    }
    
    prev = INT_MAX;
    for(int i = N - 1;  i >= 0; i--){
        if(s[i] == c)
            prev = i;
        res[i] = MIN(res[i], abs(prev - i));            
    }
    
    *returnSize = N;
    return res;
}