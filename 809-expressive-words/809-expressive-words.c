int countRepeat(char * s, int ssize,int index){
    int ptr = index;
    while(ptr < ssize && s[ptr] == s[index])
        ptr++;
    return ptr - index;
}

bool isStrechy(char * s, char * word){
    int ptr_s = 0, ptr_w = 0;
    int S = strlen(s), W = strlen(word);
    
    while(ptr_s < S && ptr_w < W){
        if(s[ptr_s] != word[ptr_w])
            return false;
        
        int countW = countRepeat(word, W, ptr_w);
        int countS = countRepeat(s, S, ptr_s);
        
        if(countW > countS)
            return false;
        if(countS != countW && countS < 3)
            return false;
        
        ptr_s += countS;
        ptr_w += countW;
    }
    
    return (ptr_s == S && ptr_w == W) ? true : false;
    
}

int expressiveWords(char * s, char ** words, int wordsSize){
    int output = 0;
    for(int i = 0; i < wordsSize; i++){
        if(isStrechy(s, words[i]))
            output++;
    }
    return output;
}