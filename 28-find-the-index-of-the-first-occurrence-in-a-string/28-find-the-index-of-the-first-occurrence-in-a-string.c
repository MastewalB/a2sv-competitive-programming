

int strStr(char * haystack, char * needle){
    int n = strlen(needle), m = strlen(haystack);
    int f[n], i = 0, j = 0;
    
    failure(f, n, needle);
    
    while(i < m){
        if(haystack[i] == needle[j]){
            if(j == n - 1)
                return i - n + 1;
            i++;
            j++;
        }else if(j > 0)
            j = f[j - 1];
        else
            i++;
    }
    return -1;
}

void failure(int * f, int fSize, char * p){
    int i = 1, j = 0;
    f[0] = 0;
    
    while(i < fSize){
        if(p[i] == p[j]){
            f[i++] = (j++) + 1;

        }
        else if(j > 0)
            j = f[j - 1];
        else
            f[i++] = 0;
    }
}