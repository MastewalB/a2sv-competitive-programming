#define MAX(a, b) (((a) > (b)) ? (a) : (b))

int longestContinuousSubstring(char * s){
    int longest = 1, count = 1, N = strlen(s);
    
    for(int i = 0; i < N; i++ ){
        if(i > 0 && s[i] - s[i - 1] == 1){
            count++;
            longest = MAX(longest, count);
        }else{
            count = 1;
        }
    }
    return longest;
}