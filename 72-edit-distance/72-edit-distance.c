#define MATCH 0
#define INSERT 1
#define DELETE 2
#define MIN(a, b) (((a) < (b)) ? (a) : (b))

int match(char s, char t){
    return (s == t) ? 0 : 1;
}


int minDistance(char * s, char * t){
    int sLen = strlen(s), tLen = strlen(t);
    int operations[3];
    
    int ** dp = (int **)calloc(sLen + 1, sizeof(int *));
    
    for(int i = 0; i <= sLen; i++){
        dp[i] = (int *)calloc(tLen + 1, sizeof(int));
        if(i == 0){
            for(int j = 0; j <= tLen; j++)
                dp[0][j] = j;
        }
        dp[i][0] = i;
        
    }
    
    for(int i = 0; i < sLen; i++){
        
        for(int j = 0; j < tLen; j++){
            
            operations[MATCH] = dp[i][j] + match(s[i], t[j]);
            operations[INSERT] = dp[i + 1][j] + 1;
            operations[DELETE] = dp[i][j + 1] + 1;
            
            dp[i + 1][j + 1] = MIN(operations[MATCH], MIN(operations[DELETE], operations[INSERT]));
        }
        
    }
    
    return dp[sLen][tLen];
    
}