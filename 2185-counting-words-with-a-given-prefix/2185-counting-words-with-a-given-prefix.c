

int prefixCount(char ** words, int wordsSize, char * pref){
    int output = 0, i, j;
    
    for(i = 0; i < wordsSize; i++){
        for(j = 0; j < strlen(pref); j++){
            if(words[i][j] == pref[j]){
                if(j == strlen(pref) - 1)
                    output++;
            }
            else break;
        }
    }
    return output;
}