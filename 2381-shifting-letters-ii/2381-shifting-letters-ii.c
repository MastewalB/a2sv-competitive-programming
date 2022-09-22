

char * shiftingLetters(char * s, int** shifts, int shiftsSize, int* shiftsColSize){
    int N = strlen(s);
    int * sweep = (int *)calloc(N + 1, sizeof(int));
    
    
    for(int i = 0; i < shiftsSize; i++){
        if(shifts[i][2] == 0) {
            sweep[shifts[i][0]] += -1;
            sweep[shifts[i][1] + 1] += 1;
        }else{
            sweep[shifts[i][0]] += 1;
            sweep[shifts[i][1] + 1] += -1;
        }
    }
    for(int i = 0; i < N; i++){
        if(i > 0)
            sweep[i] += sweep[i - 1];
        int curr = ((s[i] - 'a') + sweep[i]) % 26;
        char old = s[i];
        s[i] = (curr >= 0) ? 97 + curr : 123 + curr;
        // if(i > 420)
        //     printf("  %d %c %c %d", sweep[i], old, s[i], curr);
    }
    
    return s;
}